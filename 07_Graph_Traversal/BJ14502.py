#implementation + graph traversal(BFS)
from collections import deque
from itertools import combinations
from copy import deepcopy
sero, garo = map(int, input().split())

graph=[]
graph_linear=[i for i in range(sero*garo)]
virus_cord=[]
for i in range(sero):
    current_line = list(map(int, input().split()))
    graph.append(current_line)
for i in range(sero):
    for j in range(garo):
        if graph[i][j]==2:
            virus_cord.append([i, j])

dx=[1, -1, 0,0]
dy=[0, 0, 1, -1]
def bfs(graph, start):
    global sero, garo,  dx, dy
    q=deque()
    q.append(start)
    while q:
        current_node = q.popleft()
        for i in range(4):
            X=current_node[0]+dx[i]
            Y=current_node[1]+dy[i]
            if 0<=X<sero and 0<=Y<garo:
                if graph[X][Y]==0:
                    q.append([X, Y])
                    graph[X][Y]=2

def count_zero(sero, garo, graph):
    count=0
    for i in range(sero):
        for j in range(garo):
            if graph[i][j] ==0:
                count+=1
    return count


def make_cord(num):
    global garo
    cord=[0,0]
    cord[0] = num//garo
    cord[1] = num%garo
    return cord


result=-1
def using_wall_bfs():
    global graph_linear, graph, virus_cord, sero, garo, result
    for i in combinations(graph_linear, 3):
        first=make_cord(i[0])
        second=make_cord(i[1])
        third=make_cord(i[2])
        if graph[first[0]][first[1]]== 0 and graph[second[0]][second[1]]== 0 and graph[third[0]][third[1]]== 0:
            copy_graph = deepcopy(graph)
            copy_graph[first[0]][first[1]]= 1
            copy_graph[second[0]][second[1]]= 1
            copy_graph[third[0]][third[1]]= 1
            for virus in virus_cord:
                bfs(copy_graph, virus)
            result = max(result, count_zero(sero, garo, copy_graph))

using_wall_bfs()

print(result)




