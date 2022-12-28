import sys
import ast
from antlr4 import *
from src.cpp2llvmLexer import cpp2llvmLexer
from src.cpp2llvmParser import cpp2llvmParser
from src.cpp2llvmParserVisitor import cpp2llvmParserVisitor
from llvmlite import ir
from llvmlite.ir.types import ArrayType
from llvmlite.ir.values import GlobalVariable, ReturnValue
from tables import *

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


class myVisitor(cpp2llvmParserVisitor):
    def __init__(self):
        super().__init__()
        
        self.Module=ir.Module()
        self.Builders=[]

        self.symbolTable = SymbolTable()
        
        self.Switchexpression = []
        self.Switchcaselabel = []
        self.blockToBreak=[]
        self.blockToContinue=[]

        self.string_count = 0
        self.Module.triple="x86_64-pc-linux"
    
    def visitLiteral(self, ctx:cpp2llvmParser.LiteralContext):
        return self.visit(ctx.getChild(0))
    
    def visitIntegerLiteral(self, ctx:cpp2llvmParser.IntegerLiteralContext):
        Signed = True
        if(ctx.getText()[-2:] == 'll' or ctx.getText()[-2:] == 'LL'):
            ReturnType = int64
            if ctx.getText()[-3] == 'u' or ctx.getText()[-3] == 'U':
                Signed = False
                textOutOfSuffix = ctx.getText()[:-3]
            else:
                textOutOfSuffix = ctx.getText()[:-2]
        elif(ctx.getText()[-1]=='l' or ctx.getText()[-2:-1] == 'L'):
            ReturnType = int32
            if ctx.getText()[-2] == 'u' or ctx.getText()[-2] == 'U':
                Signed = False
                textOutOfSuffix = ctx.getText()[:-2]
            else:
                textOutOfSuffix = ctx.getText()[:-1]
        else:
            ReturnType = int32
            if ctx.getText()[-1] == 'u' or ctx.getText()[-1] == 'U':
                Signed = False
                textOutOfSuffix = ctx.getText()[:-1]
            else:
                textOutOfSuffix = ctx.getText()
        return {
            'type':ReturnType,
            'signed':Signed,
            'value':ir.Constant(ReturnType,int(textOutOfSuffix))
        }
    
    def visitCharacterLiteral(self, ctx:cpp2llvmParser.CharacterLiteralContext):
        return {
                'type':int8,
                'value':ir.Constant(int8,ord(ctx.getText()[1]))
            }
    
    def visitFloatingLiteral(self, ctx:cpp2llvmParser.FloatingLiteralContext):
        return{
            'type':double,
            'value':ir.Constant(double,float(ctx.getText()))
        }

    def visitStringLiteral(self, ctx:cpp2llvmParser.StringLiteralContext):    
        s = ast.literal_eval(ctx.getText()) + '\0'
        
        string_type = ArrayType(int8,len(s))
        string_address = ir.GlobalVariable(self.Module,string_type,'__string_'+str(self.string_count))
        string_address.linkage='internal'
        string_address.initializer=ir.Constant(string_type,None)
        string_address.initializer = ir.Constant(string_type,bytearray(s,encoding='ascii'))
        self.string_count += 1
        if(self.symbolTable.current_scope_level != 0):
            Builder = self.Builders[-1]
            string_address = Builder.gep(string_address, [ir.Constant(int32,0),ir.Constant(int32,0)], inbounds=True)
        return {
            'type' : string_type,
            'value' : string_address
        } 
    
    def visitConstExpression(self, ctx:cpp2llvmParser.ConstExpressionContext):
        return self.visit(ctx.literal())
    
    def visitLeftExpression(self, ctx:cpp2llvmParser.LeftExpressionContext):
        if(ctx.getText()[-1]==']'):    
            '''
            对应语法: Identifier (LeftBracket expression RightBracket)
            '''
            index = self.symbolTable.getProperty(ctx.getChild(0).getText())
            subscribe = self.visit(ctx.getChild(2))['value']
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                Builder = self.Builders[-1]
                Address = Builder.gep(index.get_value(),[ir.Constant(int32,0),subscribe],inbounds=True)
                ValueToReturn = Builder.load(Address)
                print("call arrayItem",ValueToReturn)
                return{
                    'type':index.get_type().element,
                    'signed':True,
                    'address':Address
                }
            else:
                raise BaseException("the array isn't defined")
            
        else:
            '''
            对应语法: leftExpression:Identifier
            '''
            symbol = self.symbolTable.getProperty(ctx.getText())
            return {
                    'type':symbol.get_type(),
                    'signed':symbol.get_signed(),
                    'address':symbol.get_value(),
                }
        
    def isExprJudge(self,realText):
        if (realText == ">"):
            return True
        elif(realText == "<"):
            return True
        elif(realText == ">="):
            return True
        elif(realText == "<="):
            return True
        elif(realText == "=="):
            return True
        elif(realText == "!="):
            return True
        else:
            return False
        
    def visitExpression(self, ctx:cpp2llvmParser.ExpressionContext):
        ChildCount=ctx.getChildCount()
        Builder = self.Builders[-1]
        if(ChildCount == 1):
            grandChildren = ctx.getChild(0).getChildCount()
            if(grandChildren):
                '''
                对应语法: expression: Literal | functionCall;
                '''
                result = self.visit(ctx.getChild(0))
                return result
            else:
                '''
                对应语法: expression: Identifier
                '''
                
                symbol = self.symbolTable.getProperty(ctx.getText())
                if( isinstance(symbol.get_type(),ir.ArrayType)):
                    return {
                        'type': symbol.get_type().element.as_pointer(),
                        'value': Builder.gep(symbol.get_value(),[ir.Constant(int32,0),ir.Constant(int32,0)],inbounds=True)
                    }
                else:
                    ret_value = Builder.load(symbol.get_value())
                    return {
                        'type':ret_value.type,
                        'signed':symbol.get_signed(),
                        'value':ret_value
                    }
        elif(ChildCount == 2):
            '''
            对应语法: expression: Not expression | Minus expression | And leftExpression
            对应语法: leftexpression MinusMinus | leftexpression PlusPlus
            '''  
            if(ctx.getChild(0).getText() == '-' or ctx.getChild(0).getText() == '!' or ctx.getChild(0).getText() == '&'):
                Builder = self.Builders[-1]
                result = self.visit(ctx.getChild(1))
                if(ctx.getChild(0).getText() == '!'):
                    if result['type'] == double:
                        ValueToReturn = Builder.fcmp_ordered('!=', result['value'], ir.Constant(int1,0))
                    else:
                        ValueToReturn = Builder.icmp_signed('!=', result['value'], ir.Constant(int1,0))
                    return {
                        'type':int1,
                        'signed':True,
                        'value':ValueToReturn
                    }
                elif(ctx.getChild(0).getText() == '-'):
                    if result['type'] == double:
                        ValueToReturn = Builder.fneg(result['value'])
                    else:
                        ValueToReturn = Builder.neg(result['value'])
                    return {
                        'type':result['type'],
                        'signed':True,
                        'value':ValueToReturn
                    }
                elif(ctx.getChild(0).getText() == '&'):
                    return {
                        'type': result['type'].as_pointer(),
                        'signed' : True,
                        'value' : result['address']
                    }
            else:
                Builder = self.Builders[-1]
                lhs = self.visit(ctx.getChild(0))
                now_value = Builder.load(lhs['address'])
                if(ctx.getChild(1).getText() == '++'):
                    ValueToReturn = Builder.add(now_value,ir.Constant(lhs['type'],1))
                else:
                    ValueToReturn = Builder.sub(now_value,ir.Constant(lhs['type'],1))
                Builder.store(ValueToReturn, lhs['address'])
                return {
                    'type':lhs['type'],
                    'signed':True,
                    'value': ValueToReturn
                }    
        elif(ChildCount > 3):
            '''
            对应语法: expression: Identifier '[' expression ']'
            '''
            index = self.symbolTable.getProperty(ctx.getChild(0).getText())
            subscribe = self.visit(ctx.getChild(2))['value']
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                Builder = self.Builders[-1]
                Address = Builder.gep(index.get_value(),[ir.Constant(int32,0),subscribe],inbounds=True)
                ValueToReturn = Builder.load(Address)
                print("call arrayItem",ValueToReturn)
                return{
                    'type':index.get_type().element,
                    'signed':True,
                    'value':ValueToReturn
                }
            else:
                raise BaseException("the array isn't defined")
        elif(ChildCount == 3 and ctx.getChild(0).getText()=='('):
            '''
            对应语法: expression: '(' expression ')'
            '''
            result = self.visit(ctx.getChild(1))
            return result
        else:
            Operation = ctx.getChild(1).getText()
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            if(self.isExprJudge(Operation)):
                '''
                对应语法:  expression: expression '==' | '!=' | '<' | '<=' | '>' | '>=' expr
                '''
                left,right = self.exprTypeConvert(left,right)
                if(left['type']==double):
                    valueToReturn = Builder.fcmp_ordered(Operation,left['value'],right['value'])
                elif(left['type']==int32 or left['type'] == int64 or left['type'] == int8 or left['type']==int1):
                    if(left['signed']):
                        valueToReturn = Builder.icmp_signed(Operation,left['value'],right['value'])
                    else:
                        valueToReturn = Builder.icmp_unsigned(Operation,left['value'],right['value'])                
                return{
                    'type':int1,
                    'signed':True,
                    'value':valueToReturn
                }
            elif(Operation == '+' or Operation == '-' or Operation == '*' or Operation == '/' or Operation == '%' or Operation == '<<' or Operation == '>>'):
                '''
                对应语法: expression: expression '+'|'-'|'*'|'/'|'%' expression
                '''
                left,right = self.exprTypeConvert(left,right)
                if(Operation == '+'):
                    if(left['type']==double):
                        valueToReturn = Builder.fadd(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.add(left['value'],right['value'])
                elif(Operation == '-'):
                    if(left['type']==double): 
                        valueToReturn = Builder.fsub(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.sub(left['value'],right['value'])
                elif(Operation == '*'):
                    if left['type']==double:
                        valueToReturn = Builder.fmul(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.mul(left['value'],right['value'])
                elif(Operation == '/'):
                    if left['type'] == double:
                        valueToReturn = Builder.fdiv(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.sdiv(left['value'],right['value'])
                elif(Operation == '%'):
                    if left['type']==double:
                        valueToReturn = Builder.srem(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.frem(left['value'],right['value'])
                elif(Operation == '<<'):
                    valueToReturn = Builder.shl(left['value'],right['value'])
                elif(Operation == '>>'):
                    valueToReturn = Builder.lshr(left['value'],right['value'])
                return{
                    'type':right['type'],
                    'signed':True,
                    'value':valueToReturn
                }
            elif(Operation == '='):
                '''
                对应语法:  expression: leftExpression '=' expression
                '''
                ChildCount=ctx.getChild(0).getChildCount()
                print(left," is an varible")

                right = self.assignTypeConvert(left,right)
                Builder.store(right['value'],left['address'])
                return {
                    'type':right['type'],   
                    'value': Builder.load(left['address'])
                }
            elif(Operation == '|'  or Operation == '&'  or Operation == '^'):
                '''
                对应语法:  expression: expression Or|And|Caret expression
                '''
                left,right = self.exprTypeConvert(left,right)
                Signed = False
                if left['signed'] or right['signed']:
                    Signed = True
                if(Operation == '|' or Operation == 'bitor'):
                    ValueToReturn = Builder.or_(left['value'],right['value'])
                elif(Operation == '&' or Operation == 'bitand' ):
                    ValueToReturn = Builder.and_(left['value'],right['value'])
                elif(Operation == '^' or Operation == 'xor'):
                    ValueToReturn = Builder.xor(left['value'],right['value'])
                return{
                    'type':left['type'],
                    'signed':Signed,
                    'value':ValueToReturn
                }
            elif(Operation == '&&' or Operation == 'and' or Operation == '||' or Operation == 'or'):
                '''
                对应语法: expression AND|OR expression
                '''
                left = self.toBool(left)
                right = self.toBool(right)
                if(Operation == '&&' or Operation == 'and'):
                    ValueToReturn = Builder.and_(left['value'],right['value'])
                elif(Operation == '||' or Operation == 'or'):
                    ValueToReturn = Builder.or_(left['value'],right['value'])
                return{
                    'type':int1,
                    'signed':True,
                    'value':ValueToReturn
                }
    
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

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = cpp2llvmLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = cpp2llvmParser(stream)
    tree = parser.translationUnit()
    ast = tree.toStringTree(recog=parser)
    print(ast)
    visitor = myVisitor()
    visitor.visit(tree)
    
    outputfile = "output.ll"
    if len(argv) >= 3:
        outputfile = argv[2]
    with open(outputfile, "w") as f:
        f.write(str(visitor.Module))
    
if __name__ == '__main__':
    main(sys.argv)