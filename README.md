## start in ubuntu/wsl
* install antlr4
* pip install antlr4-python3-runtime
* antlr4 -Dlanguage=Python3 ./grammar/cpp2llvmLexer.g4 -Xexact-output-dir -o src
* python main.py <inputfile>