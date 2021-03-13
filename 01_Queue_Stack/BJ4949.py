while 1:
    is_balanced = True
    string=input().rstrip()
    if string == '.':
        break
    stack=[]
    for letter in string:
        if letter == '(' or letter=='[':
            stack.append(letter)
        elif letter == ')':
            if len(stack)>0 and stack[len(stack)-1] == '(':
                stack.pop()
            else:
                is_balanced=False
                break
        elif letter == ']':
            if len(stack)>0 and stack[len(stack)-1] == '[':
                stack.pop()
            else:
                is_balanced=False
                break
    if len(stack) !=0:
        is_balanced=False
    if is_balanced:
        print('yes')
    else:
        print('no')