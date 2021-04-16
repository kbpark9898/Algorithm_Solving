#완전탐색으로 분류했지만 bfs + 완탐으로 푼 문제!

import sys
from collections import deque
from itertools import combinations
buildings, way = map(int, sys.stdin.readline().split())
INF = 100
visited=[[100 for i in range(buildings+1)] for i in range(buildings+1)]
way_list=[[]for i in range(buildings+1)]
for i in range(buildings+1):
    for j in range(buildings+1):
        if i==j:
            visited[i][j] = 0

for i in range(way):
    start, end = map(int, sys.stdin.readline().split())
    way_list[start].append(end)
    way_list[end].append(start)


def bfs(buildings, way, visited, start, way_list):
    global INF
    q = deque()
    q.append(start)
    while q:
        current_node = q.popleft()
        for i in way_list[current_node]:
            if visited[start][i] == INF:
                visited[start][i] = visited[start][current_node]+1
                q.append(i)
    
def nearest(visited, buildings):
    solution=10000000
    solution_cord=[-1, -1]
    for comb in combinations(range(1, buildings+1), 2):
        current_solution=0
        for i in range(1, buildings+1):
            current_distance_first = visited[i][comb[0]]*2
            current_distance_second = visited[i][comb[1]]*2
            current_solution+=min(current_distance_first, current_distance_second)
        if solution>current_solution:
            solution_cord[0] = comb[0]
            solution_cord[1] = comb[1]
            solution = current_solution
        elif solution == current_solution:
            if solution_cord[0] > comb[0]:
                solution_cord[0] = comb[0]
                solution_cord[1] = comb[1]
            elif solution_cord[0] == comb[0]:
                if solution_cord[1] > comb[1]:
                    solution_cord[0] = comb[0]
                    solution_cord[1] = comb[1]
    return [solution_cord, solution]

    
for i in range(1, buildings+1):
    bfs(buildings, way, visited, i, way_list)

solution = nearest(visited, buildings)

solution[0].sort()

print(solution[0][0], solution[0][1], solution[1])
