import heapq
n = 1
MAX = 16000

def dstra(cur_graph, N):
    global MAX
    distance = [[MAX for i in range(N)] for j in range(N)]
    h = []
    heapq.heapify(h)
    heapq.heappush(h, [cur_graph[0][0], [0,0]])
    distance[0][0] = cur_graph[0][0]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while h:
        cur_node = heapq.heappop(h)
        cur_cord = cur_node[1]
        cur_distance = cur_node[0]
        for i in range(4):
            next_cord = [cur_cord[0]+dx[i], cur_cord[1]+dy[i]]
            if 0<=next_cord[0]<N and 0<=next_cord[1]<N:
                next_distance = cur_distance+cur_graph[next_cord[0]][next_cord[1]]
                if next_distance < distance[next_cord[0]][next_cord[1]]:
                    distance[next_cord[0]][next_cord[1]] = next_distance
                    heapq.heappush(h, [next_distance, [next_cord[0], next_cord[1]]])
    return distance[N-1][N-1]

stage = 1
result = []
while 1:
    n = int(input())
    if n == 0:
        break
    graph=[]
    for i in range(n):
        graph.append(list(map(int, input().split())))
    cur_result = dstra(graph, n)
    result.append(f'Problem {stage}: {cur_result}')
    stage+=1


for i in result:
    print(i)
