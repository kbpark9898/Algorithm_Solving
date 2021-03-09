#BFS 이용한 풀이. 풀리긴 한다!
from collections import deque

testcase=int(input())
graph=[]
visited=[]
for i in range(testcase):
    nations, flight = map(int, input().split())
    current_visited=[0 for k in range(nations+1)]
    current_graph=[[0 for i in range(nations+1)] for i in range(nations+1)]
    for j in range(flight):
        source, dst = map(int, input().split())
        current_graph[source][dst] = 1
        current_graph[dst][source] = 1
    graph.append(current_graph)
    visited.append(current_visited)

answer=[]
start=1
def bfs(node, cur_v, cur_g):
    q=deque()
    v=cur_v
    g=cur_g
    v[node]=1
    q.append(node)
    count=-1
    while q:
        current_node = q.popleft()
        count+=1
        for i in range(1, len(v)):
            if v[i] == 0 and g[current_node][i]==1:
                q.append(i)
                v[i] = 1
    return count
    

            
    
for i in range(testcase):
    current_graph = graph[i]
    current_visited=visited[i]
    answer.append(bfs(start, current_visited, current_graph))

for i in range(len(answer)):
    print(answer[i])

    



