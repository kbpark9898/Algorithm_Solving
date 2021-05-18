from collections import deque
import heapq

cases = int(input())
MAX = 200000000
def dstra(adj, visited, start):
    q = []
    heapq.heapify(q)
    heapq.heappush(q, start)
    visited[start[1]] = 0
    last_node=[]
    while q:
        cur_node = heapq.heappop(q)
        for adj_node in adj[cur_node[1]]:
            if visited[adj_node[1]] > visited[cur_node[1]] + adj_node[0]:
                visited[adj_node[1]] = visited[cur_node[1]] + adj_node[0]
                heapq.heappush(q, [visited[adj_node[1]], adj_node[1]])

def count_node(visited):
    result=0
    time=0
    for i in range(1, len(visited)):
        if visited[i] != MAX:
            result+=1
            time = max(time, visited[i])
    return [result, time]

solution=[]
for i in range(cases):
    n, d, c = map(int, input().split())
    adj=[[]for i in range(n+1)]
    visited=[ MAX for i in range(n+1)]
    for j in range(d):
        src, dst, cost = map(int, input().split())
        adj[dst].append([cost, src])
    dstra(adj, visited, [0, c])
    result = count_node(visited)
    solution.append([result[0], result[1]])

for i in solution:
    print(i[0], i[1])



