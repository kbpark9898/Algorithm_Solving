
import sys
left_stack = list(sys.stdin.readline().strip())
right_stack = []

commands = int(input())

for i in range(commands):
    command = sys.stdin.readline().strip()
    if command=='L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command=='D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command=='B':
        if left_stack:
            left_stack.pop()
    else:
        command = list(command)
        left_stack.append(command[2])

result=''.join(left_stack+list(reversed(right_stack)))

print(result)