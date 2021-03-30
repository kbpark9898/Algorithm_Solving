from collections import deque
string=list(input())
explode=list(input())


solution = deque()

for item in string:
    solution.append(item)
    if len(solution)>=len(explode):
        is_explode = True
        for k in range(len(explode)):
            if solution[len(solution)-len(explode)+k] != explode[k]:
                is_explode=False
        if is_explode:
            for i in range(len(explode)):
                solution.pop()
if solution:
    print(''.join(solution))
else:
    print("FRULA")

