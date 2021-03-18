# BFS의 색다른 용도와, 메모리 최적화까지 생각하게 해준 명문제!
from collections import deque
start, target=map(int, input().split())
visited={}
def bfs(start, targrt):
    global visited
    q = deque()
    q.append(start)
    visited[start]=1
    while q:
        current_node = q.popleft()
        double = current_node*2
        append_one = int(str(current_node)+'1')
        if double == target or append_one==target:
            visited[target]=visited[current_node]+1
            return
        if double < target and double not in visited:
            q.append(double)
            visited[double]=visited[current_node]+1
        if append_one < target and append_one not in visited:
            q.append(append_one)
            visited[append_one]=visited[current_node]+1

bfs(start, target)
if target not in visited:
    print(-1)
else:
    print(visited[target])
        