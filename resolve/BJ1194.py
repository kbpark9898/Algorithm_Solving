from collections import deque

sero, garo = map(int, input().split())
key_hash = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5}
door_hash = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}

graph=[]

for i in range(sero):
    graph.append(input())


def find_src(graph):
    global sero
    global garo
    for i in range(sero):
        for j in range(garo):
            if graph[i][j] == '0':
                return [0, i, j]


def key_compare(cur_keys, key):
    global key_hash
    return (cur_keys | (1<<key_hash[key]))

def door_compare(cur_keys, door):
    global door_hash
    return (cur_keys & (1<<door_hash[door]))


def bfs():
    global sero
    global garo
    global graph
    global key_hash
    global door_hash
    visited = [[[0 for i in range(garo)]for j in range(sero)] for k in range(64)]
    q = deque()
    start_point = find_src(graph)
    q.append(start_point)
    visited[start_point[0]][start_point[1]][start_point[2]] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        cur_node = q.popleft()
        for i in range(4):
            X = cur_node[1] + dx[i]
            Y = cur_node[2] + dy[i]
            if 0<=X<sero and 0<=Y<garo and visited[cur_node[0]][X][Y] == 0:
                if graph[X][Y] == '1':
                    return  visited[cur_node[0]][cur_node[1]][cur_node[2]]
                elif graph[X][Y] in ('0', '.'):
                    q.append([cur_node[0], X, Y])
                    visited[cur_node[0]][X][Y] = visited[cur_node[0]][cur_node[1]][cur_node[2]]+1
                elif graph[X][Y] in key_hash:
                    key_compare_result = key_compare(cur_node[0], graph[X][Y])
                    q.append([key_compare_result, X, Y])
                    visited[key_compare_result][X][Y] = visited[cur_node[0]][cur_node[1]][cur_node[2]]+1
                elif graph[X][Y] in door_hash:
                    door_compare_result = door_compare(cur_node[0], graph[X][Y])
                    if door_compare_result:
                        q.append([cur_node[0], X, Y])
                        visited[cur_node[0]][X][Y] = visited[cur_node[0]][cur_node[1]][cur_node[2]]+1
    return False

result = bfs()

if result != False:
    print(result)
else:
    print(-1)

                    



