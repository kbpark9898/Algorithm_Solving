from collections import deque
import copy
n, l, r = map(int, input().split())

graph= []
for i in range(n):
    cur_list = list(map(int, input().split()))
    graph.append(cur_list)

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
visited=[[0 for i in range(n)] for j in range(n)]
section_id = 1

def can_move(before_cord, after_cord):
    global graph, l, r
    if(l<=abs(graph[before_cord[0]][before_cord[1]] - graph[after_cord[0]][after_cord[1]])<=r):
        return True
    else:
        return False
def bfs(cur_cord):
    global graph, dx, dy, n, visited, section_id
    visited_count = 1
    visited_Ingu = graph[cur_cord[0]][cur_cord[1]]
    q = deque()
    q.append(cur_cord)
    visited[cur_cord[0]][cur_cord[1]] = section_id
    while q:
        cur_node = q.popleft()
        for i in range(4):
            X = cur_node[0] + dx[i]
            Y = cur_node[1] + dy[i]
            if(0<=X<n and 0<=Y<n and visited[X][Y] == 0 and can_move([cur_node[0], cur_node[1]], [X, Y])):
                q.append([X, Y])
                visited[X][Y] = section_id
                visited_count+=1
                visited_Ingu += graph[X][Y]
    return [visited_count, visited_Ingu, visited]


def ingu_move( n, bfs_result, graph, section_id):
    result_population = bfs_result[1] // bfs_result[0]
    for i in range(n):
        for j in range(n):
            if(bfs_result[2][i][j] == section_id):
                graph[i][j] = result_population

result = 0
def play(n, graph):
    global visited, result, section_id
    while 1:
        before_graph = copy.deepcopy(graph)
        for i in range(n):
            for j in range(n):
                if(visited[i][j] == 0):
                    cur_result = bfs([i, j])
                    if(cur_result[0] == 1):
                        visited[i][j] = 0
                    else:
                        ingu_move(n, cur_result, graph, section_id)
                        section_id+=1
                    
        section_id = 1
        visited=[[0 for i in range(n)] for j in range(n)]
        if(before_graph == graph):
            return
        else:
            result+=1



play(n, graph)
print(result)
