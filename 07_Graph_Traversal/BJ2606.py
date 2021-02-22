node_count=int(input())
edge_count=int(input())

node_list=[[0]*(node_count+1) for i in range(node_count+1)]
visited=[0]*(node_count+1)

for i in range(edge_count):
    start_node, end_node = map(int, input().split())
    node_list[start_node][end_node]=1
    node_list[end_node][start_node]=1


count=0

def dfs(start):
    global visited
    global node_list
    global count
    visited[start]=1
    for i in range(1, node_count+1):
        if visited[i] ==0 and node_list[start][i] ==1:
            count+=1
            dfs(i)

dfs(1)
print(count)