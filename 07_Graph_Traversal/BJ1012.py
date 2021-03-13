from collections import deque
test_case = int(input())



dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def bfs(graph, visited, x, y):
    global dx, dy
    q=deque()
    q.append([x, y])
    visited[x][y]=1
    while q:
        current_node = q.pop()
        for i in range(4):
            X = current_node[0] + dx[i]
            Y = current_node[1] + dy[i]
            if X>=0 and X<sero and Y>=0 and Y<garo:
                if visited[X][Y] ==0 and graph[X][Y]==1:
                    q.append([X, Y])
                    visited[X][Y]=1

answer=[]
for i in range(test_case):
    result=0
    garo, sero, bachu = map(int, input().split())
    graph=[[0 for i in range(garo+1)] for i in range(sero+1)]
    visited=[[0 for i in range(garo+1)] for i in range(sero+1)]
    for j in range(bachu):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(sero):
        for j in range(garo):
            if graph[i][j] ==1 and visited[i][j] !=1:
                bfs(graph, visited, i, j)
                result+=1
    answer.append(result)


for i in answer:
    print(i)