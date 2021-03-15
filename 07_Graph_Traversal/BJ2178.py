from collections import deque 

sero, garo = map(int, input().split())

graph=[]
visited=[]

def make_graph(graph, visit, n):
    for i in range(n):
        path = list(input())
        visit_data=[]
        for i in range(len(path)):
            path[i] = int(path[i])
            visit_data.append(0)
        graph.append(path)
        visit.append(visit_data)


dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def bfs(graph, visited, start):
    global dx, dy, sero, garo
    q= deque()
    q.append(start)
    visited[start[0]][start[1]]=1
    while q:
        current_node = q.popleft()
        for i in range(4):
            X = current_node[0] + dx[i]
            Y = current_node[1] + dy[i]
            if X>=0 and X<sero and Y>=0 and Y<garo:
                if visited[X][Y] ==0 and graph[X][Y] ==1:
                    q.append([X,Y])
                    visited[X][Y] = visited[current_node[0]][current_node[1]]+1
                    
          
                    
make_graph(graph, visited, sero)

bfs(graph, visited, [0,0])
print(visited[sero-1][garo-1])


