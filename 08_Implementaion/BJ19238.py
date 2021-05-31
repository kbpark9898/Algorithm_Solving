#implementaion + simulation + BFS
import sys
import heapq
from collections import deque
if __name__ == "__main__":
    n, m, fuel = map(int, sys.stdin.readline().split())

    graph=[]
    for i in range(n):
        cur_list=list(map(int, sys.stdin.readline().split()))
        graph.append(cur_list)

    taxi_src = list(map(int, sys.stdin.readline().split()))
    src_dst=[]
    for i in range(m):
        x, y, x_, y_ = map(int, sys.stdin.readline().split())
        src_dst.append([[x, y], [x_, y_]])


    is_taken=[False for i in range(m)]

    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]

    def bfs():
        global n, m, fuel, graph, taxi_src, src_dst, is_taken, dx, dy
        q = deque()
        q.append([taxi_src[0]-1, taxi_src[1]-1])
        visited=[[-1 for i in range(n)] for i in range(n)]
        visited[taxi_src[0]-1][taxi_src[1]-1] = 0
        while q:
            cur_node = q.popleft()
            for i in range(4):
                X = cur_node[0] + dx[i]
                Y = cur_node[1] + dy[i]
                if 0<=X<n and 0<=Y<n and graph[X][Y] == 0 and visited[X][Y] == -1:
                    visited[X][Y] = visited[cur_node[0]][cur_node[1]]+1
                    q.append([X,Y])
        return visited

    def next_person():
        global n, m, fuel, graph, taxi_src, src_dst, is_taken, dx, dy
        bfs_result = bfs()
        q = []
        for i in range(m):
            if is_taken[i] == False:
                x = src_dst[i][0][0]-1
                y = src_dst[i][0][1]-1
                distance = bfs_result[x][y]
                #도달할 수 없는 경우를 간과하여 최초 제출 실패. distance != 1 을 추가해서 도달할 수 없는 경우를 필터링.
                if distance != -1 and fuel - distance >=0:
                    heapq.heappush(q, [distance, x, y, i])
        if not q:
            return -1
        else:
            cur_node = heapq.heappop(q)
            fuel -= cur_node[0]
            is_taken[cur_node[3]] = True
            return cur_node[3]


    def next_target(src_idx):
        global n, m, fuel, graph, taxi_src, src_dst, is_taken, dx, dy
        bfs_result = bfs()
        cur_dst=[src_dst[src_idx][1][0], src_dst[src_idx][1][1]]
        cost = bfs_result[cur_dst[0]-1][cur_dst[1]-1]
        if fuel - cost >=0:
            return cost
        else:
            return -1

    is_possible = True
    def play(m):
        global is_possible, fuel, taxi_src, src_dst
        count = m
        while count:
            src_idx = next_person()
            if src_idx==-1:
                is_possible = False
                break
            taxi_src = src_dst[src_idx][0]
            cost = next_target(src_idx)
            if cost == -1:
                is_possible = False
                break
            fuel += cost
            taxi_src=src_dst[src_idx][1]
            count-=1
        if is_possible:
            print(fuel)
        else:
            print(-1)

    play(m)