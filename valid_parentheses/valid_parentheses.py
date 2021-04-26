def valid_parentheses(string: str):
    if len(string) == 0:
        return True
    if (len(string) % 2) > 0:
        return False
    
    dict = {']':'[', ')':'(', '}':'{'}
    
    stack = []
    
    for i in range(len(string)):
        char = string[i]
        if i > 0:
            if char in dict and stack[-1] == dict[char]:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    
    if len(stack):
        return False
    return True


if __name__ == '__main__':
    
    print(valid_parentheses('{([])}'))
    print(valid_parentheses('{([])]'))
    print(valid_parentheses('{([)]}'))
    print(valid_parentheses(''))
    print(valid_parentheses('{([]'))
    print(valid_parentheses('{[(])}'))
    print(valid_parentheses('{[]()}'))