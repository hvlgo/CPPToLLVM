## start in ubuntu/wsl

### install java

* sudo apt update

* sudo apt upgrade

* sudo apt install openjdk-11-jdk

### install antlr4

* cd /usr/local/lib

* sudo curl -O https://www.antlr.org/download/antlr-4.11.1-complete.jar

* add follow to `.bashrc` or run it (if just run it, you need run it again when create a new terminal)

  ```shell
  export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"
  alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
  alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
  ```

### install python support

* pip install antlr4-python3-runtime

### generate python file according to grammar

* antlr4 -Dlanguage=Python3 ./grammar/cpp2llvmLexer.g4 ./grammar/cpp2llvmParser.g4 -Xexact-output-dir -o src -visitor

### run parser and get the abstract syntax tree
python main.py \<inputfile> \<outputfile>

### install llvm

* sudo apt-get install clang-format clang-tidy clang-tools clang clangd libc++-dev libc++1 libc++abi-dev libc++abi1 libclang-dev libclang1 liblldb-dev libllvm-ocaml-dev libomp-dev libomp5 lld lldb llvm-dev llvm-runtime llvm python3-clang

### run *.ll file
lli \<outputfile>