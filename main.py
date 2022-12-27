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