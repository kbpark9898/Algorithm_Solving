# 시작할때 불은 한군데가 아니라 여러곳에 붙어있을 수 있다.

from collections import deque
sero, garo = map(int, input().split())

graph = []
for i in range(sero):
    graph.append(input())

jihun_cord=[]
fire_cord = []
visited=[['#' for i in range(garo)]for j in range(sero)]

for i in range(sero):
    for j in range(garo):
        if graph[i][j] == 'J':
            jihun_cord = [i, j, 'J',1]
        elif graph[i][j] == 'F':
            fire_cord.append([i, j, 'F'])
        elif graph[i][j] == '.':
            visited[i][j] = '.'



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    global graph
    global jihun_cord
    global fire_cord
    global dx
    global dy
    global garo
    global sero
    result = 1
    if jihun_cord[0] in (0,sero-1) or jihun_cord[1] in (0,garo-1):
        return 1
    q = deque()
    for cord in fire_cord:
        q.append(cord)
        visited[cord[0]][cord[1]] = 'F'
    q.append(jihun_cord)
    visited[jihun_cord[0]][jihun_cord[1]] = 'J'
    while(q):
        cur_node = q.popleft()
        cur_x = cur_node[0]
        cur_y = cur_node[1]
        cur_id = cur_node[2]
        if((cur_x in(0,sero-1) or cur_y in (0,garo-1) ) and cur_id == 'J'):
            return cur_node[3]
        for i in range(4):
            X = cur_x+dx[i]
            Y = cur_y+dy[i]
            if 0<=X<sero and 0<=Y<garo:
                if visited[X][Y] == '.' and cur_id == 'J':
                    visited[X][Y] = cur_id
                    q.append([X,Y,cur_id, cur_node[3]+1])
                elif visited[X][Y] in ('.', 'J') and cur_id == 'F':
                    visited[X][Y] = cur_id
                    q.append([X,Y,cur_id])
    return False


result = bfs()
if result == False:
    print('IMPOSSIBLE')
else:
    print(result)

            

