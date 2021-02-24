# 아 BFS 너무 어렵다

from collections import deque
sero, garo = map(int, input().split())
graph=[]
for i in range(sero):
    data=list(map(int, input()))
    graph.append(data)

visited=[[[0]*2 for i in range(1001)]for j in range(1001)]
result=[[[0]*2 for i in range(garo)]for j in range(sero)]
q=deque()
q.append([0,0,1])
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
result[0][0][1] = 1
def bfs():
    global visited
    global q
    while q:
        length = len(q)
        for i in range(length):
            current_node = q.popleft()
            if current_node[0] == sero-1 and current_node[1] == garo-1:
                if current_node[2] ==1:
                    return 1
                else:
                    return 2
            for j in range(4):
                broken=current_node[2]
                X = current_node[0]+dx[j]
                Y = current_node[1]+dy[j]
                if 0>X or X==sero or 0>Y or Y==garo:
                    continue
                if broken ==0:
                    if graph[X][Y] ==0:
                        if visited[X][Y][0] ==0:
                            visited[X][Y][0] = 1
                            result[X][Y][0] = result[current_node[0]][current_node[1]][0]+1
                            q.append([X, Y, 0])
                else:
                    if graph[X][Y]==0:
                        if visited[X][Y][1] ==0:
                            visited[X][Y][1]=1
                            result[X][Y][1] = result[current_node[0]][current_node[1]][1]+1
                            q.append([X, Y, 1])
                    else:
                        if visited[X][Y][0] ==0:
                            visited[X][Y][0] = 1
                            result[X][Y][0] = result[current_node[0]][current_node[1]][1]+1
                            q.append([X,Y,0])
    return 0

answer = bfs()
if answer==1:
    print(result[sero-1][garo-1][1])
elif answer ==2:
    print(result[sero-1][garo-1][0])
else:
    print(-1)
