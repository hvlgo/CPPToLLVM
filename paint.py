import re
import json

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
                
        

        
    # print(right_node)
    # 加入children
    # children.append(toJsonNode)
    # children.append(toJsonNode)
    return dict


if __name__ == "__main__":
    # raw_str = "(name1 (name2 (name3 int)) name4 <EOF>)"
    file = open("tree.txt", "r")
    raw_str = file.read()
    file.close()
    # print(raw_str)
    test_str = raw_str[:-7] + ')'
    # print(test_str)
    root = toJsonNode(test_str)

    with open("record.json","w") as f:
        json.dump(root, f, indent=2, ensure_ascii=False)
        print("加载入文件完成...")