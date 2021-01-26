from collections import deque
import heapq
task_q = []
solution_B=deque()
solution_R=deque()
last_time_B = 0
last_time_R = 0
k = list(map(int, input().split()))
for i in range(k[2]):
    input_task = input().split()
    input_task[0] = int(input_task[0])
    input_task[2] = int(input_task[2])
    if input_task[1]=='B':
        t = input_task[0]
        sum_t=input_task[0]
        if last_time_B > t:
            t = last_time_B
            sum_t = last_time_B
        for j in range(input_task[2]):
            heapq.heappush(task_q, (t, input_task[1]))
            t+=k[0]
        last_time_B = sum_t + input_task[2]*k[0]
    else:
        t = input_task[0]
        sum_t = input_task[0]
        if last_time_R > t:
            t = last_time_R
            sum_t = last_time_R
        for j in range(input_task[2]):
            heapq.heappush(task_q, (t, input_task[1]))
            t+=k[1]
        last_time_R = sum_t + input_task[2]*k[1]

order_num=1
for i in range(len(task_q)):
    data = heapq.heappop(task_q)
    if data[1] =='B':
        solution_B.append(str(order_num))
        order_num+=1
    else:
        solution_R.append(str(order_num))
        order_num+=1
print(len(solution_B))
print(' '.join(solution_B))
print(len(solution_R))
print(' '.join(solution_R))
