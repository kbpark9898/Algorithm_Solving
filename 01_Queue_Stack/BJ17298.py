import sys
from collections import deque
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

number_stack=[]
result=deque()

for i in range(n-1, -1, -1):
    if not number_stack:
        number_stack.append(numbers[i])
        result.appendleft(-1)
    else:
        is_breaked=False
        while number_stack:
            stack_top = number_stack[len(number_stack)-1]
            if numbers[i] < stack_top:
                number_stack.append(numbers[i])
                result.appendleft(stack_top)
                is_breaked = True
                break
            elif numbers[i] >= stack_top:
                number_stack.pop()
        if not is_breaked:
            number_stack.append(numbers[i])
            result.appendleft(-1)

for i in result:
    print(i, end=' ')


