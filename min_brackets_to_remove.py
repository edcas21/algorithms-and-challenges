def min_brackets_to_remove(string: str):
    dict = {'(':')'}
    stack = []
    for i in range(len(string)):
        # current character
        char = string[i]
        # if current char isn't a lowecase character
        if not char.islower():
            # make sure the stack isn't empty
            if len(stack):
                # stack stores indices, so get the char that corresponds to the index in the stack
                stack_char = string[stack[-1]]
                # if stack_char is an opening bracket and the current char is equal to a closing bracket
                if stack_char in dict and dict[stack_char] == char:
                    # pop the top index from the stack since it's corresponding closing bracket has been found
                    stack.pop()
                else:
                    # if no corresponding bracket has been found, just push the index onto the stack
                    stack.append(i)
            else:
                # the stack is empty to push first bracket found
                stack.append(i)
    # return string that has all the characters who's index is not in the stack
    return ''.join([string[i] for i in range(len(string)) if i not in stack])

if __name__ == '__main__':
    test_cases = ['a)bc(d)', '(ab(c)d', '))((']
    for test_case in test_cases:
        res = min_brackets_to_remove(test_case)
        print(res)