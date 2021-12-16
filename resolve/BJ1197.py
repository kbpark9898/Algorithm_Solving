nodes, edges = map(int, input().split())
graph=[]
for i in range(edges):
    src, dst, cost = map(int, input().split())
    graph.append([cost, src, dst])

graph.sort()

parents=[i for i in range(nodes+1)]

def find(a):
    global parents
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    global parents
    root_a = find(a)
    root_b = find(b)
    parents[root_b] = root_a

def kruskal():
    global graph
    global nodes
    global parents
    edge_count = 0
    answer = 0
    while len(graph)>0:
        if edge_count == nodes-1:
            break
        cur_edge = graph.pop(0)
        if find(cur_edge[1]) != find(cur_edge[2]):
            union(cur_edge[1], cur_edge[2])
            answer+=cur_edge[0]
            edge_count+=1
    return answer

result = kruskal()

print(result)