from collections import deque
k = int(input())
solution_task = deque()
solution_time =deque()
solution_score = 0
for i in range(k):
    input_data = list(map(int, input().split()))
    if input_data[0] !=0:
        solution_task.append(input_data[1])
        solution_time.append(input_data[2])
    if len(solution_task)!=0:
        solution_time[-1]-=1
        if solution_time[-1]==0:
            solution_time.pop()
            solution_score+=solution_task.pop()
print(solution_score)
 

