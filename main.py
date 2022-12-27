import sys
from antlr4 import *
from src.cpp2llvmLexer import cpp2llvmLexer
from src.cpp2llvmParser import cpp2llvmParser
from src.cpp2llvmParserVisitor import cpp2llvmParserVisitor

class myVisitor(cpp2llvmParserVisitor):
    def __init__(self):
        pass

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