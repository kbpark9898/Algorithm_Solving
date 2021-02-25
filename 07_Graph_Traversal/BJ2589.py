from collections import deque
sero, garo = map(int, input().split())
Jido =[]
for i in range(sero):
    Jido.append(list(map(str, input())))
visited=[]
for i in range(sero):
    _data=[]
    for j in range(garo):
        _data.append(0)
    visited.append(_data)

q=deque()

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
max_distance=-1
coord=[]
def find_max(mapdata):
    global sero, garo
    current = mapdata[0][0]
    for i in range(sero):
        for j in range(garo):
            if current<mapdata[i][j]:
                current = mapdata[i][j]          
    return current

def bfs(x, y):
    global sero, garo, Jido, q, visited, max_distance, dx, dy
    q.append([x, y])
    while q:
        length = len(q)
        for i in range(length):
            current_node = q.popleft()
            for j in range(4):
                X=current_node[0]+dx[j]
                Y=current_node[1]+dy[j]
                if X<0 or X==sero or Y<0 or Y==garo:
                    continue
                if visited[X][Y] ==0 and Jido[X][Y] == 'L':
                    visited[X][Y] += visited[current_node[0]][current_node[1]]+1
                    visited[x][y]=1
                    q.append([X, Y])
    
    max_distance = max(max_distance, find_max(visited))

    for i in range(sero):
        for j in range(garo):
            visited[i][j]=0

for i in range(sero):
    for j in range(garo):
        if Jido[i][j] == 'L':
            bfs(i, j)

print(max_distance)







    
