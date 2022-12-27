import sys
from antlr4 import *
from src.cpp2llvmLexer import cpp2llvmLexer
from src.cpp2llvmParser import cpp2llvmParser
from src.cpp2llvmParserVisitor import cpp2llvmParserVisitor
from llvmlite import ir
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