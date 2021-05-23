nodes, edges = map(int, input().split())

graph=[]
parents=[i for i in range(nodes+1)]
for i in range(edges):
    src, dst, cost = map(int, input().split())
    graph.append([cost, src, dst])

graph.sort()

def find(a):
    global parents
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    parents[root_b] = root_a


solution=0
edge_count=0
def kruskal():
    global graph, solution, edge_count
    while 1:
        if edge_count == nodes-1:
            return
        current_edge = graph.pop(0)
        if find(current_edge[1]) != find(current_edge[2]):
            union(current_edge[1], current_edge[2])
            solution+=current_edge[0]
            edge_count+=1

kruskal()

print(solution)
