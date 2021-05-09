from collections import deque
# BFS + 비트마스크
sero, garo = map(int, input().split())
graph=[]
for i in range(sero):
    current_input = list(input())
    graph.append(current_input)


def find_source(graph):
    global sero, garo
    for i in range(sero):
        for j in range(garo):
            if graph[i][j]=='0':
                return [i, j, 0]

visited=[[[0 for i in range(garo)]for i in range(sero)]for i in range(64)]

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def key_shift_and_compare(current_key, new_key, key_hash):
    result = current_key | (1<<key_hash[new_key])
    return result

def door_shift_and_compare(current_key, door, door_hash):
    result = current_key & (1<<door_hash[door])
    return result
    
def bfs(start, graph):
    global sero, garo, visited, dx, dy
    key={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5}
    door = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
    q=deque()
    q.append(start)
    visited[start[2]][start[0]][start[1]]=1
    while q:
        current_node = q.popleft()
        for i in range(4):
            X = current_node[0] + dx[i]
            Y = current_node[1] + dy[i]
            if 0<=X<sero and 0<=Y<garo and visited[current_node[2]][X][Y] == 0:
                if graph[X][Y]  =='1':
                    return visited[current_node[2]][current_node[0]][current_node[1]]+1
                elif graph[X][Y] in ('.', '0'):
                    q.append([X, Y, current_node[2]])
                    visited[current_node[2]][X][Y] = visited[current_node[2]][current_node[0]][current_node[1]]+1
                elif graph[X][Y] in key:
                    new_node=[X, Y, key_shift_and_compare(current_node[2], graph[X][Y], key)]
                    visited[new_node[2]][new_node[0]][new_node[1]] = visited[current_node[2]][current_node[0]][current_node[1]]+1
                    q.append(new_node)
                elif graph[X][Y] in door:
                    result = door_shift_and_compare(current_node[2], graph[X][Y], door)
                    if result:
                        q.append([X, Y, current_node[2]])
                        visited[current_node[2]][X][Y] = visited[current_node[2]][current_node[0]][current_node[1]]+1

def play():
    global graph
    source = find_source(graph)
    result = bfs(source, graph)
    if result:
        print(result-1)
    else:
        print(-1)

play()




        



