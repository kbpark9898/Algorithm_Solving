#음수 가중치가 없는 경우 최단거리 : 다익스트라.

import heapq

towns = int(input())
bus = int(input())
INF=100000000
adj=[[]for i in range(towns+1)]
cost=[INF for i in range(towns+1)]
for i in range(bus):
    source, destination, weight = map(int, input().split())
    adj[source].append([destination, weight])

source, dst = map(int, input().split())

def dijkstra(adj, cost, start, end):
    q=[]
    heapq.heapify(q)
    heapq.heappush(q, [0, start])
    cost[start]=0
    while q:
        current_node= heapq.heappop(q)
        for adj_node in adj[current_node[1]]:
            new_distance = current_node[0] + adj_node[1]
            if cost[adj_node[0]] > new_distance:
                cost[adj_node[0]] = new_distance
                heapq.heappush(q, [new_distance, adj_node[0]])

dijkstra(adj, cost, source, dst)
print(cost[dst])

        
