import sys
from collections import deque
sys.setrecursionlimit(100000)
def dfs(cur, start, count):
    global is_cycle,visited
    if cur == start and count>=2:
        is_cycle=True
        return
    
    visited[cur] =1
    for node in adj_list[cur]:
        if visited[node] == 0:
            dfs(node, start, count+1)
        elif node == start and count>=2:
            dfs(node, start, count)
    

def bfs():
    global adj_list, cycle_nodes, answer
    bfs_visited=[0 for i in range(n+1)]
    q = deque()
    for i in range(1, len(cycle_nodes)):
        if cycle_nodes[i] == 1:
            answer[i] = 0
            q.append(i)
    while q:
        current_node = q.popleft()
        for node in adj_list[current_node]:
            if answer[node] == -1:
                answer[node] = answer[current_node]+1
                q.append(node)


def play():
    global answer
    for i in range(1,len(answer)):
        print(answer[i], end=" ")
    

n=int(input())
adj_list=[[]for i in range(n+1)]
for i in range(n):
    src, dst = map(int, input().split())
    adj_list[src].append(dst)
    adj_list[dst].append(src)

is_cycle=False
visited=[0 for i in range(n+1)]
cycle_nodes=[0 for i in range(n+1)]

answer=[-1 for i in range(n+1)]

for i in range(1, n+1):
    is_cycle=False
    visited=[0 for i in range(n+1)]
    dfs(i, i, 0)
    if is_cycle:
        cycle_nodes[i] = 1

bfs()
play()
    
