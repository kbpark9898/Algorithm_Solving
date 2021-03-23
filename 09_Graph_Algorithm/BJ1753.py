import heapq

v, e = map(int, input().split())
k = int(input())

adj = [[]for i in range(v+1)]
INF=10000000

distance=[INF for i in range(v+1)]

for i in range(e):
    source, dst, weight = map(int, input().split())
    adj[source].append([dst, weight]) 


def dijkstra(start):
    global adj, distance
    q = []
    heapq.heapify(q)
    heapq.heappush(q, [0,start])
    distance[start] = 0
    while q:
        current_node = heapq.heappop(q)
        for adj_node in adj[current_node[1]]:
            dst = adj_node[0]
            weight = adj_node[1]
            new_distance = current_node[0] + weight
            if distance[dst] > new_distance:
                distance[dst]=new_distance
                heapq.heappush(q, [new_distance, dst])

dijkstra(k)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])