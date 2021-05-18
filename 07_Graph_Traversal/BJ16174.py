from collections import deque
n = int(input())
graph=[]
for i in range(n):
    current_list = list(map(int, input().split()))
    graph.append(current_list)


visited=[[0 for i in range(n)]for i in range(n)]

dx=[1, 0]
dy=[0, 1]
def bfs():
    global n, graph, visited, dx, dy
    q=deque()
    q.append([0,0])
    visited[0][0] = 1
    while q:
        current_node = q.popleft()
        for i in range(2):
            X = current_node[0] + dx[i]*graph[current_node[0]][current_node[1]]
            Y = current_node[1] + dy[i]*graph[current_node[0]][current_node[1]]
            if 0<=X<n and 0<=Y<n and visited[X][Y] == 0:
                if graph[X][Y] == -1:
                    visited[n-1][n-1] = 1
                    return
                q.append([X, Y])
                visited[X][Y] = 1

bfs()
if visited[n-1][n-1] == 1:
    print("HaruHaru")
else:
    print("Hing")