def check_correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if len(stack) == 0:
                return False
            if stack[len(stack)-1] == '(':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

def split_u_v(string):
    u=''
    v=''
    left_count = 0
    right_count = 0
    for s in string:
        if s == '(':
            u+=s
            left_count+=1
        else:
            u+=s
            right_count+=1
        if left_count == right_count:
            break
    v = string[len(u):]
    return[u, v]

    

def play(p):
    if len(p) == 0:
        return ''
    u, v = split_u_v(p)
    if check_correct(u):
        return u+play(v)
    else:
        u = u[1:-1]
        new_u=''
        for letter in u:
            if letter == ')':
                new_u+='('
            else:
                new_u+=')'
        return '(' + play(v) + ')' +new_u
        
    

def solution(p):
    answer = play(p)
    return answer
