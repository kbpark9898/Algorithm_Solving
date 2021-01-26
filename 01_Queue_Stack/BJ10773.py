k=int(input())
solution_stack=[]
solution=0
for i in range(k):
    n=int(input())
    if n==0:
        solution_stack.pop()
    else:
        solution_stack.append(n)
for i in range(len(solution_stack)):
    solution+=solution_stack[i]
print(solution)