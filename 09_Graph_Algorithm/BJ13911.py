import heapq

n, edges = map(int, input().split())

MAX = 1000000000

graph=[[]for i in range(n+3)]

for i in range(edges):
    src, dst, w = map(int, input().split())
    graph[src].append([dst, w])
    graph[dst].append([src, w])


mac_=list(map(int, input().split()))
Macdonalds = list(map(int, input().split()))
star_=list(map(int, input().split()))
starbucks = list(map(int, input().split()))

for mac in Macdonalds:
    graph[mac].append([n+1, 0])
    graph[n+1].append([mac, 0])

for star in starbucks:
    graph[star].append([n+2, 0])
    graph[n+2].append([star, 0])

mac_adj = [MAX for i in range(n+3)]
star_adj = [MAX for i in range(n+3)]
mac_adj[n+1] = 0
star_adj[n+2] = 0
def dstra(start, graph, adj):
    global n
    heap=[]
    heapq.heappush(heap, [0, start])
    adj[start] = 0
    while heap:
        cur_dis, cur_node = heapq.heappop(heap)
        for dst, dis in graph[cur_node]:
            if dst == n+1 or dst == n+2:
                continue
            new_dis = dis + cur_dis
            if adj[dst] > new_dis:
                adj[dst] = new_dis
                heapq.heappush(heap, [new_dis, dst])

dstra(n+1, graph, mac_adj)
dstra(n+2, graph, star_adj)


result = MAX
for node in range(1, n+1):
    if not(node in Macdonalds or node in starbucks):
        if mac_adj[node] <= mac_[1] and star_adj[node] <= star_[1]:
            result = min(result, mac_adj[node] + star_adj[node])
            
        

if result == MAX:
    print(-1)
else:
    print(result)

