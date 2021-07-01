from collections import deque
from copy import deepcopy
m_dx=[1, -1, 0, 0]
m_dy=[0, 0, 1, -1]

h_d=[(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

k = int(input())
garo, sero = map(int, input().split())

graph=[]


temp_graph=[]
for i in range(sero):
    cur_list = list(map(int, input().split()))
    temp_graph.append(cur_list)

for i in range(k+1):
    t = deepcopy(temp_graph)
    graph.append(t)

start=[0,0,k]

def bfs(start):
    global m_dx, m_dy, h_d, sero, garo
    q = deque()
    q.append(start)
    graph[start[2]][start[0]][start[1]] += 1
    while q :
        cur_node = q.popleft()
        before_x = cur_node[0]
        before_y = cur_node[1]
        before_k = cur_node[2]
        if before_x == sero -1 and before_y == garo-1 : break
        if before_k>0:
            for i in range(8):
                cur_x = before_x + h_d[i][0]
                cur_y = before_y + h_d[i][1]
                cur_k = before_k-1
                if 0<=cur_x<sero and 0<=cur_y<garo and graph[cur_k][cur_x][cur_y] == 0:
                    q.append([cur_x, cur_y, cur_k])
                    graph[cur_k][cur_x][cur_y]= graph[before_k][before_x][before_y]+1
            for i in range(4):
                cur_x = before_x + m_dx[i]
                cur_y = before_y + m_dy[i]
                cur_k = before_k
                if 0<=cur_x<sero and 0<=cur_y<garo and graph[cur_k][cur_x][cur_y] == 0:
                    q.append([cur_x, cur_y, cur_k])
                    graph[cur_k][cur_x][cur_y]=graph[before_k][before_x][before_y]+1
        else:
            for i in range(4):
                cur_x = before_x + m_dx[i]
                cur_y = before_y + m_dy[i]
                cur_k = before_k
                if 0<=cur_x<sero and 0<=cur_y<garo and graph[cur_k][cur_x][cur_y] == 0:
                    q.append([cur_x, cur_y, cur_k])
                    graph[cur_k][cur_x][cur_y]=graph[before_k][before_x][before_y]+1


bfs(start)
result = 400000
for t_graph in graph:
    if t_graph[sero-1][garo-1] != 0:
        result = min(result, t_graph[sero-1][garo-1])


if result == 400000:
    print(-1)
else:
    print(result -1)



    


