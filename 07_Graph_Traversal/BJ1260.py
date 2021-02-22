from queue import Queue
node_count, edge_count, start=map(int, input().split())
node_list=[[0]*(node_count+1) for i in range(node_count+1)]

for i in range(edge_count):
    first_node, second_node = map(int, input().split())
    node_list[first_node][second_node]=1
    node_list[second_node][first_node]=1
visited=[0]*(node_count+1)
dfs_result=[]
bfs_result=[]


def dfs(s):
    global dfs_result
    global visited
    visited[s]=1
    dfs_result.append(s)
    for i in range(1, node_count+1):
        if visited[i]==0 and node_list[s][i]==1:
            dfs(i)


def bfs(s, r):
    q=Queue()
    q.put(s)
    global visited
    visited[s]=0
    r.append(s)
    while not q.empty():
        current_node = q.get()
        for i in range(node_count+1):
            if visited[i]==1 and node_list[current_node][i]==1:
                q.put(i)
                visited[i]=0
                r.append(i)


dfs(start)
bfs(start,bfs_result)

for i in dfs_result:
    print(i, end=' ')
print()
for i in bfs_result:
    print(i, end=' ')
            