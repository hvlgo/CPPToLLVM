import sys
from antlr4 import *
from src.cpp2llvmLexer import cpp2llvmLexer

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = cpp2llvmLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()
    ls = [str(token) for token in stream.tokens][:-1]
    for i in ls:
        print(i)
    # parser = cpp2llvmParser(stream)
    # tree = parser.translationUnit()
    # print(tree.toStringTree())

if __name__ == '__main__':
    main(sys.argv)