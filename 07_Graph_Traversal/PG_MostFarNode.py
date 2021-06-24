#https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def bfs(graph, visited, n):
    q=deque()
    q.append([1,0])
    visited[1] =0
    while q:
        cur_node = q.popleft()
        for node in graph[cur_node[0]]:
            if visited[node] == -1:
                q.append([node, cur_node[1]+1])
                visited[node] = cur_node[1]+1


def find_max_nodes(visited):
    cur_max = -1
    max_count=0
    for node in visited:
        if node == cur_max:
            max_count+=1
        elif node > cur_max:
            cur_max = node
            max_count = 1
    return max_count

        
def solution(n, edge):
    visited = [-1 for i in range(n+1)]
    graph=[[] for i in range(n+1)]
    for i in range(len(edge)):
        src, dst = edge[i]
        graph[src].append(dst)
        graph[dst].append(src)
    
    bfs(graph, visited, n)
    answer = find_max_nodes(visited)
    return answer
