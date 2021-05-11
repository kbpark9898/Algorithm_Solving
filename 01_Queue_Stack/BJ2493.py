import sys
n = int(input())
towers = list(map(int, sys.stdin.readline().split()))
result=[]

tower_stack=[]

for i in range(n):
    if not tower_stack:
        tower_stack.append((i+1,towers[i]))
        result.append(0)
    else:
        is_breaked=False
        while tower_stack:
            stack_top = tower_stack[len(tower_stack)-1]
            if towers[i] > stack_top[1]:
                tower_stack.pop()
            else:
                result.append(stack_top[0])
                tower_stack.append((i+1, towers[i]))
                is_breaked=True
                break
        if not is_breaked:
            result.append(0)
            tower_stack.append((i+1, towers[i]))
                

for i in result:
    print(i, end=' ')

