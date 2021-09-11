import heapq

n = int(input())
MAX = 100000001

def dstra(start, adj, visited):
    h = []
    heapq.heappush(h, start)
    visited[start[1]] = 0
    while h:
        cur_node = heapq.heappop(h)
        for adj_node in adj[cur_node[1]]:
            if visited[adj_node[1]] > visited[cur_node[1]] + adj_node[0]:
                visited[adj_node[1]] = visited[cur_node[1]] + adj_node[0]
                heapq.heappush(h, [visited[adj_node[1]], adj_node[1]])


def find_infected_node(visited):
    global MAX
    count = 0
    time = 0
    for i in range(len(visited)):
        if visited[i] <MAX:
            count+=1
            time = max(time, visited[i])
    return [count, time]


for i in range(n):
    n, d, c = map(int, input().split())
    adj=[[] for j in range(n+1)]
    visited=[MAX for j in range(n+1)]
    for l in range(d):
        dst, src, cost = map(int, input().split())
        adj[src].append([cost, dst])
    dstra([0, c], adj, visited)
    result = find_infected_node(visited)
    print(result[0], result[1])