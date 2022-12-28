import sys
import re
import json
from antlr4 import *
from src.cpp2llvmLexer import cpp2llvmLexer
from src.cpp2llvmParser import cpp2llvmParser
from src.cpp2llvmParserListener import cpp2llvmParserListener as cpp2llvmListener
from src.cpp2llvmParserVisitor import cpp2llvmParserVisitor as cpp2llvmVisitor
from llvmlite import ir

from llvmlite.ir.types import ArrayType
from llvmlite.ir.values import GlobalVariable, ReturnValue

double = ir.DoubleType()
int1 = ir.IntType(1)
int8 = ir.IntType(8)
int16 = ir.IntType(16)
int32 = ir.IntType(32)
int64 = ir.IntType(64)
void = ir.VoidType()

int8p = ir.PointerType(int8)
int16p = ir.PointerType(int16)
int32p = ir.PointerType(int32)
int64p = ir.PointerType(int64)
doublep = ir.PointerType(double)

def toJsonNode(input):
    dict = {
        'name': '',
        'children': []    
    }
    # print(input)
    try:
        # 获取name
        # 内部节点
        if input[0] == '(' and len(input) > 1:
            dict['name'] = str(re.search(r'\(\S+', input).group(0))[1:]
        # 叶子节点
        else:
            # dict['name'] = str(re.search(r'\S+', input).group(0))
            dict['name'] = input
            return dict
    except Exception as e:
        print(e)
        print(input)
    # print(dict)

    # 解析子节点, 后括号去掉
    new_str = input[len(dict['name'])+2:-1]
    # print(new_str)

    stack_total = 0
    flag = False        # 进入括号的标志
    left = right = 0
    for char in new_str:
        if not flag:
            if char != ' ':
                right += 1
                # 到最后一个
                if right >= len(new_str):
                    dict['children'].append(toJsonNode(new_str[left:right]))
                    return dict
 
                if char == '(' :
                    # 需要解析的
                    if new_str[right] == ')' or new_str[right] == ' ':
                        continue
                    flag = True
                    stack_total += 1
                    left = right - 1
            else:
                dict['children'].append(toJsonNode(new_str[left:right]))
                left = right = right + 1
        else:
            right += 1
            if right >= len(new_str):
                dict['children'].append(toJsonNode(new_str[left:right]))
                return dict
            if char == '(' and new_str[right] != ')' and new_str[right] != ' ':
                stack_total += 1
            elif char == ')' and new_str[right-2] != ' ':
                stack_total -= 1
            
            if stack_total == 0:
                flag = False
    return dict

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = cpp2llvmLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = cpp2llvmParser(stream)
    tree = parser.translationUnit()
    ast = tree.toStringTree(recog=parser)
    print(ast)
    root = toJsonNode(ast)
    outputfile = "record.json"
    if len(argv) >= 3:
        outputfile = argv[2]
    with open(outputfile, "w") as f:
        json.dump(root, f, indent=2, ensure_ascii=False)

class myCpp20Visitor(cpp2llvmVisitor):
    def __init__(self):
        super(cpp2llvmVisitor,self).__init__()
        
        self.Module=ir.Module()

        self.Builders=[]

        # 符号表
        # self.symbolTable = NameTable()
        

        self.Switchexpression = []

        self.Switchcaselabel = []


        self.blockToBreak=[]
        self.blockToContinue=[]

        # 全局字符串的数量
        self.string_count = 0

        self.Module.triple="x86_64-pc-linux"

    
    # utils
    def toBool(self, result):
        Builder = self.Builders[-1]
        if result['type'] == double:
            ValueToReturn = Builder.fcmp_ordered('!=', result['value'], ir.Constant(int1,0))
        else:
            ValueToReturn = Builder.icmp_signed('!=', result['value'], ir.Constant(int1,0))
        return{
            'type':int1,
            'signed':True,
            'value':ValueToReturn
        }

    #left和right的符号类型不一致时，类型转换为一致，向大的类型转换
    def exprTypeConvert(self,left,right):
        if(left['type']==right['type']):
            return left,right
        elif self.isInt(left) and self.isInt(right):
            if left['type'].width < right['type'].width:
                left = self.intConvert(left,right)
            else:
                right = self.intConvert(right,left)
        elif self.isInt(left) and right['type']==double: 
            left = self.intToDouble(left)
        elif left['type']==double and self.isInt(right):
            right = self.intToDouble(right)
        return left, right

    def visitReturnStatement(self, ctx: cpp2llvmParser.ReturnStatementContext):
        # returnStatement : Return expression? Semi;
        if ctx.expression() is None:
            # Return from the current function without a value.
            self.Builders[-1].ret_void()    
        else:
            # Return the value from the current function.
            self.Builders[-1].ret(self.visit(ctx.expression())['value'])
        return

    def visitBreakStatement(self, ctx: cpp2llvmParser.BreakStatementContext):
        # breakStatement : Break Semi;

        if self.blockToBreak:
            Builder = self.Builders[-1]
            Builder.branch(self.blockToBreak[-1])
        else:
            raise BaseException("cannot break")        
        return

    def visitContinueStatement(self, ctx: cpp2llvmParser.ContinueStatementContext):
        # continueStatement : Continue Semi;

        if self.blockToContinue:
            Builder = self.Builders[-1]
            Builder.branch(self.blockToContinue[-1])
        else:
            raise BaseException("cannot continue")
        return

    def visitCompoundStatement(self, ctx: cpp2llvmParser.CompoundStatementContext):
        # compoundStatement: LeftBrace statement* RightBrace;
        
        self.symbolTable.enterScope()
        super().visitCompoundStatement(ctx)
        self.symbolTable.exitScope()

        return

    def visitWhileStatement(self, ctx: cpp2llvmParser.WhileStatementContext):
        # whileStatement : While LeftParen expression RightParen statement;
        Builder = self.Builders[-1]
        
        expressionBlock = Builder.append_basic_block()      # 判断
        whileStatementBlock = Builder.append_basic_block()  # 循环体
        endWhileBlock = Builder.append_basic_block()        # 退出循环

        self.blockToBreak.append(endWhileBlock)
        self.blockToContinue.append(expressionBlock)

        #expressionBlock
        Builder.branch(expressionBlock)
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(expressionBlock))
        result = self.visit(ctx.getChild(2))
        condition = self.toBool(result)
        self.Builders[-1].cbranch(condition['value'],whileStatementBlock,endWhileBlock)
        
        #whileStatementBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(whileStatementBlock))
        self.visit(ctx.getChild(4))
        if not self.Builders[-1].block.is_terminated:
            self.Builders[-1].branch(expressionBlock)

        #endWhileBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(endWhileBlock))

        self.blockToContinue.pop()
        self.blockToBreak.pop()

        return 

    def visitDoWhileStatement(self, ctx: cpp2llvmParser.DoWhileStatementContext):
        # doWhileStatement : Do statement While LeftParen expression RightParen Semi;
        Builder = self.Builders[-1]


        doStatementBlock = Builder.append_basic_block()
        expressionBlock = Builder.append_basic_block()
        endWhileBlock = Builder.append_basic_block()

        self.blockToBreak.append(endWhileBlock)
        self.blockToContinue.append(expressionBlock)

        #doStatementBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(doStatementBlock))
        self.visit(ctx.getChild(1))
        if(not self.Builders[-1].block.is_terminated):
            self.Builders[-1].branch(expressionBlock)

        #expressionBlock
        self.Builders[-1].branch(expressionBlock)
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(expressionBlock))
        result = self.visit(ctx.getChild(4))
        condition = self.toBool(result)
        self.Builders[-1].cbranch(condition['value'],doStatementBlock,endWhileBlock)

        #endWhileBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(endWhileBlock))
        
        self.blockToContinue.pop()
        self.blockToBreak.pop()
        
        return


    def visitForStatement(self, ctx: cpp2llvmParser.ForStatementContext):
        # forStatement : For LeftParen forExprSet? Semi expression? Semi forExprSet? RightParen statement;
        # forExprSet: expression (Comma expression)*;

        Builder = self.Builders[-1]
        
        # 是否三个expression都有
        ChildCount = ctx.getChildCount()
        flag1 = flag2 = flag3 = True

        # 第一个没有
        if(ctx.getChild(2).getText()==';'):
            flag1 = False
        

        for i in range(ChildCount-1):
            text1 = ctx.getChild(i).getText()
            text2 = ctx.getChild(i+1).getText()
            if(text1 == ';' and text2 != ';'):
                # 找到expression位置
                expressionIndex = i + 1
                break
            # 都是分号，说明中间的expression没有
            if(text1 == text2):
                flag2 = False
        
        # 第三个没有
        if(ctx.getChild(ChildCount-3).getText()==';'):
            flag3 = False
        
        #运行第一个forExprSet的语句
        if(flag1):
            self.visit(ctx.getChild(2))

        JudgeBlock = Builder.append_basic_block()       # 判断
        loopBlock = Builder.append_basic_block()        # 循环体    
        forExprBlock = Builder.append_basic_block()    # 循环变量
        endLoopBlock = Builder.append_basic_block()     # 退出循环
        
        self.blockToBreak.append(endLoopBlock)
        self.blockToContinue.append(forExprBlock)
        
        #JudgeBlock
        if(flag2):
            self.Builders[-1].branch(JudgeBlock)
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(JudgeBlock))
            result = self.visit(ctx.getChild(expressionIndex))
            condition = self.toBool(result)
            self.Builders[-1].cbranch(condition['value'], loopBlock, endLoopBlock)

        #loopBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(loopBlock))
        self.visit(ctx.getChild(ChildCount-1))
        if(not self.Builders[-1].block.is_terminated):
            self.Builders[-1].branch(forExprBlock)

        #forExprBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(forExprBlock))
        if(flag3):
            self.visit(ctx.getChild(ChildCount-3))
        if(flag2):
            self.Builders[-1].branch(JudgeBlock)
        else:
            self.Builders[-1].branch(loopBlock)    


        #endLoopBlock
        self.Builders.pop() 
        self.Builders.append(ir.IRBuilder(endLoopBlock))
        
        self.blockToBreak.pop()
        self.blockToContinue.pop()
            
        return

    
    def visitIfStatement(self, ctx: cpp2llvmParser.IfStatementContext):
        # ifStatement : If LeftParen expression RightParen statement (Else statement)?;

        self.symbolTable.enterScope()
        Builder = self.Builders[-1]

        trueBlock = Builder.append_basic_block()

        #if else
        if len(ctx.statement()) == 2:
            falseBlock = Builder.append_basic_block()
            endBlock = Builder.append_basic_block()
            
            #条件跳转
            result = self.visit(ctx.getChild(2))
            condition = self.toBool(result)
            Builder.cbranch(condition['value'], trueBlock, falseBlock)
            
            # if
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(trueBlock))
            self.visit(ctx.getChild(4))
            if not self.Builders[-1].block.is_terminated:
                self.Builders[-1].branch(endBlock)
            
            # else
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(falseBlock))
            self.visit(ctx.getChild(6))
            if not self.Builders[-1].block.is_terminated:
                self.Builders[-1].branch(endBlock)
            
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(endBlock))
            
        #只有if没有else
        else:
            endBlock = Builder.append_basic_block()
            
            #条件跳转
            result = self.visit(ctx.getChild(2))
            condition = self.toBool(result)
            Builder.cbranch(condition['value'], trueBlock, endBlock)
            
            #if块
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(trueBlock))
            self.visit(ctx.getChild(4))
            if(not self.Builders[-1].block.is_terminated):
                self.Builders[-1].branch(endBlock)
            
            #endif标识符
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(endBlock))

        self.symbolTable.exitScope()

        return
        

    def visitSwitchStatement(self, ctx: cpp2llvmParser.SwitchStatementContext):
        # switchStatement : Switch LeftParen expression RightParen LeftBrace (caseStatement)* RightBrace;

        self.symbolTable.enterScope()

        caseNum = ctx.getChildCount()-6
        Builder = self.Builders[-1]
        
        result = self.visit(ctx.getChild(2))
        self.Switchexpression.append(result)
        
        # 每个case一个判断块，一个执行块，外加一个结束switch块
        temp = []
        for i in range(caseNum * 2 + 2):
            temp.append(Builder.append_basic_block())
        self.Switchcaselabel.append(temp)
        self.blockToBreak.append(temp[-1])  # 最后一个块是退出switch
        
        Builder.branch(temp[0])
        
        for i in range(caseNum):
            self.visit(ctx.getChild(i+5))
        
        assert len(self.Switchcaselabel[-1]) == 2
        # 依次判断执行
        ir.IRBuilder(self.Switchcaselabel[-1][0]).branch(self.Switchcaselabel[-1][1])
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(self.Switchcaselabel[-1][1]))
        
        self.Switchexpression.pop()
        self.Switchcaselabel.pop()
        self.blockToBreak.pop()
        
        self.symbolTable.exitScope()

        return


    def visitCaseStatement(self, ctx: cpp2llvmParser.CaseStatementContext):
        # caseStatement: Case constExpression Colon statement;

        self.symbolTable.enterScope()

        judgeBlock = self.Switchcaselabel[-1][0]
        statementBlock = self.Switchcaselabel[-1][1]
        targetJudgeBlock = self.Switchcaselabel[-1][2]
        targetStatementBlock = self.Switchcaselabel[-1][3]
        
        judgeBuilder = ir.IRBuilder(judgeBlock)
        
        left = self.Switchexpression[-1]
        right = self.visit(ctx.getChild(1))
            
        left,right = self.exprTypeConvert(left,right)
        Operation = '=='
        if(left['type']==double):
            valueToReturn = judgeBuilder.fcmp_ordered(Operation,left['value'],right['value'])
        elif(left['type']==int32 or left['type'] == int64 or left['type'] == int8 or left['type']==int1):
            if(left['signed']):
                valueToReturn = judgeBuilder.icmp_signed(Operation,left['value'],right['value'])
            else:
                valueToReturn = judgeBuilder.icmp_unsigned(Operation,left['value'],right['value'])                
        
        judgeBuilder.cbranch(valueToReturn, statementBlock, targetJudgeBlock)
        
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(statementBlock))
        self.visit(ctx.getChild(3))
        if not self.Builders[-1].block.is_terminated:
            self.Builders[-1].branch(targetStatementBlock)
        
        self.symbolTable.exitScope()
        
        # 移除第一个case
        self.Switchcaselabel[-1].pop(0) 
        self.Switchcaselabel[-1].pop(0)

        return
    

if __name__ == '__main__':
    main(sys.argv)