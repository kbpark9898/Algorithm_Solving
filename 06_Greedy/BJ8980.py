n, c = map(int, input().split())
m = int(input())
tasks=[]


for i in range(m):
    cur_task = list(map(int, input().split()))
    tasks.append(cur_task)

tasks = sorted(tasks, key=lambda tasks: (tasks[1]))

remain_truck=[c for i in range(n+1)]
result=0
for task in tasks:
    current_box=c
    for i in range(task[0], task[1]):
        current_box = min(current_box, remain_truck[i], task[2])
    for i in range(task[0], task[1]):
        remain_truck[i]-=current_box
    result+=current_box
print(result)
            

