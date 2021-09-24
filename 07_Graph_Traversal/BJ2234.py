from collections import deque
garo, sero = map(int, input().split())

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
wall_key={
    0: 8,
    1: 2,
    2: 4,
    3: 1
}

wall=[1, 2, 4, 8]

graph=[]
graphs=[]
for i in range(sero):
    cur_list = list(map(int, input().split()))
    graph.append(cur_list)

visited=[[0 for i in range(garo)] for i in range(sero)]


def can_go(x, y, visited, target, wall_key_value):
    global garo, sero
    if 0<=x<sero and 0<=y<garo and visited[x][y] == 0 and target & wall_key_value == 0:
        return True
    else:
        return False


def bfs(graph, start, visited, secstion_number):
    global dx, dy, sero, garo, wall_key
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = secstion_number
    cur_section_size = 1
    while q:
        cur_node = q.popleft()
        for i in range(4):
            X = cur_node[0]+dx[i]
            Y = cur_node[1]+dy[i]
            if can_go(X, Y, visited, graph[cur_node[0]][cur_node[1]], wall_key[i]) == True:
                q.append([X, Y])
                visited[X][Y] = secstion_number
                cur_section_size+=1
    return cur_section_size

#하나의 그래프를 전부 탐색하기위해 bfs를 호출하는 함수
def play_for_one_graph(graph):
    global garo, sero
    visited=[[0 for i in range(garo)] for i in range(sero)]
    section_number = 0
    max_section = -1
    for i in range(sero):
        for j in range(garo):
            if visited[i][j] == 0:
                section_number+=1
                max_section = max(max_section, bfs(graph, [i,j], visited, section_number))
                
    return[section_number, max_section]


first_second_answer = play_for_one_graph(graph)

third_answer = -1

for i in range(sero):
    for j in range(garo):
        if graph[i][j] != 0:
            for key in wall_key:
                if graph[i][j] & wall_key[key] != 0:
                    graph[i][j] -= wall_key[key]
                    third_answer = max(third_answer, play_for_one_graph(graph)[1])
                    graph[i][j] += wall_key[key]
                    

first_second_answer.append(third_answer)

for i in first_second_answer:
    print(i)
