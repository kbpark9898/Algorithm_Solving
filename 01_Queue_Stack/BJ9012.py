k= int(input())
for i in range(k):
    VFS=input()
    solution_stack=[]
    is_VFS=True
    is_printed=False
    for i in VFS:
        if i=='(':
            solution_stack.append(i)
        else:
            if len(solution_stack)==0:
                print('NO')
                is_VFS=False
                is_printed=True
                break
            else:
                solution_stack.pop()
    if is_VFS==True and len(solution_stack)==0:
        print('YES')
    else:
        if is_printed:
            is_VFS=True
        else:
            is_VFS=True
            is_printed=False
            print('NO')
