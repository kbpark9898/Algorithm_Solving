from collections import deque

islands, bridges = map(int, input().split())

graph=[[]for i in range(islands+1)]

for i in range(bridges):
    src, dst, cost = map(int, input().split())
    graph[src].append([cost, dst])
    graph[dst].append([cost, src])



src, dst = map(int, input().split())
def check(mid, graph):
    global islands
    global bridges
    global src
    global dst
    visited=[0 for i in range(islands+1)]
    q = deque()
    q.append(src)
    visited[src] = 1
    while q:
        cur_node = q.popleft()
        if cur_node == dst:
            return True
        for next_node in graph[cur_node]:
            if visited[next_node[1]] == 0 and next_node[0] >= mid:
                q.append(next_node[1])
                visited[next_node[1]] = 1
    return False

def p_search(graph):
    left, right = 1, 1000000001
    while left <= right:
        mid = (left+right)//2
        if check(mid, graph):
            left = mid+1
        else:
            right = mid-1
    return (left+right)//2

result = p_search(graph)

print(result)


