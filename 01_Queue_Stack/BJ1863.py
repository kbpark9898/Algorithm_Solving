k = int(input())

stack=[]
solution=0
for i in range(k):
    x , y = map(int, input().split())
    while stack and stack[len(stack)-1] > y:
        stack.pop()
        solution+=1
    if stack and stack[len(stack)-1] == y:
        continue
    stack.append(y)

while stack:
    data = stack.pop()
    if data>0:
        solution+=1

print(solution)
