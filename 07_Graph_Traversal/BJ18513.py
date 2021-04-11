import sys
from collections import deque
n, k= map(int, sys.stdin.readline().split())
pond = list(map(int, sys.stdin.readline().split()))

visited = {}
for i in pond:
    visited[i] = 1

def bfs(n, k , pond, visited):
    house_count=0
    solution=0
    dx=[1, -1]
    q=deque()
    for i in pond:
        q.append([i, i])
    while q :
        current_node = q.popleft()
        for i in range(2):
            X = current_node[0]+dx[i]
            if X not in visited :
                q.append([X, current_node[1]])
                visited[X]=1
                house_count+=1
                solution+=abs(current_node[1] - X)
            if house_count>=k:
                return solution
    return solution

solution = bfs(n, k, pond, visited)
print(solution)



