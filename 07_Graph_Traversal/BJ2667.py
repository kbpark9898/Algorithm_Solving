from queue import Queue
import sys
k=int(input())
house=[list(map(int, list(input()))) for i in range(k)]


visited=[[0]*k for i in range(k)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
result=0
def dfs(x, y):
    global visited
    global k
    global house
    global result
    visited[x][y] = 1
    result+=1
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if X<0 or X==k or Y<0 or Y==k:
            continue
        if visited[X][Y] ==0 and house[X][Y]==1:
            dfs(X, Y)
            

answer=[]
cnt=0
for i in range(k):
    for j in range(k):
        if visited[i][j] ==0 and house[i][j]==1:
            result=0
            dfs(i, j)
            cnt+=1
            answer.append(result)
            

answer.sort()
print(cnt)
for i in range(len(answer)):
    print(answer[i])

    