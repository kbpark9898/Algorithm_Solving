k=int(input())
adjust_list=[[]for i in range(k+1)]
for i in range(k):
    _data = list(map(int, input().split()))
    length = len(_data)
    for j in range(1, length//2):
        adjust_list[_data[0]].append([_data[2*j-1], _data[2*j]])


first_DFS=[0 for i in range(k+1)]

def dfs(adjust, start, result):
    for a, b in adjust[start]:
        if result[a] ==0:
            result[a] = result[start] + b
            dfs(adjust, a, result)

dfs(adjust_list, 1, first_DFS)
first_DFS[1]=0


second_DFS = [0 for i in range(k+1)]

max_node=0
max_distance=0

for i in range(len(first_DFS)):
    if first_DFS[i] > max_distance:
        max_node = i
        max_distance=first_DFS[i]

dfs(adjust_list, max_node, second_DFS)
second_DFS[max_node] = 0
result = max(second_DFS)
print(result)
