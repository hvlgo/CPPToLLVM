import sys
import re
import json
from antlr4 import *
from src.cpp2llvmLexer import cpp2llvmLexer
from src.cpp2llvmParser import cpp2llvmParser

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

if __name__ == '__main__':
    main(sys.argv)