from collections import deque
k = int(input())
graph=[]
for i in range(k):
    current_input=list(input())
    graph.append(current_input)

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def color_bfs(visited, param, node):
    global graph, k, dx, dy
    q = deque()
    q.append(node)
    visited[node[0]][node[1]]=1
    while q:
        current_node = q.popleft()
        for i in range(4):
            X = current_node[0] + dx[i]
            Y = current_node[1] + dy[i]
            if 0<=X<k and 0<=Y<k:
                if visited[X][Y] == 0 and graph[X][Y] == param:
                    q.append([X,Y])
                    visited[X][Y]=1
def colorblind_bfs(visited, param, node):
    global graph, k, dx, dy
    q = deque()
    q.append(node)
    visited[node[0]][node[1]]=1
    while q:
        current_node = q.popleft()
        for i in range(4):
            X = current_node[0] + dx[i]
            Y = current_node[1] + dy[i]
            if 0<=X<k and 0<=Y<k:
                if param=='R' or param=='G':
                    if visited[X][Y] == 0 and (graph[X][Y] == 'R' or graph[X][Y]=='G'):
                        q.append([X,Y])
                        visited[X][Y]=1
                else:
                    if visited[X][Y] == 0 and graph[X][Y] == param:
                        q.append([X,Y])
                        visited[X][Y]=1


color=['R', 'G', 'B']
result={'R':0, 'G':0, 'B':0 }
blind_result={'R':0 ,'G':0, 'B':0 }
visited=[[0 for i in range(k)] for i in range(k)]
blind_visited=[[0 for i in range(k)] for i in range(k)]
for i in color:
    for garo in range(k):
        for sero in range(k):
            if visited[garo][sero] == 0 and graph[garo][sero] == i:
                color_bfs(visited, i, [garo, sero])
                result[i]+=1
            if blind_visited[garo][sero]==0 and graph[garo][sero] == i:
                colorblind_bfs(blind_visited, i, [garo, sero])
                blind_result[i]+=1

print(result['R']+result['G']+result['B'], blind_result['R']+blind_result['G']+blind_result['B'])