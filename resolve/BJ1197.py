nodes, edges = map(int, input().split())

graph=[]
for i in range(edges):
    src, dst, cost = map(int ,input().split())
    graph.append([cost, src, dst])

graph.sort()


parants = [i for i in range(nodes+1)]

def find(a):
    global parants
    if a != parants[a]:
        parants[a] = find(parants[a])
    return parants[a]

def union(a, b):
    global parants
    a_root = find(a)
    b_root = find(b)
    parants[b_root] = a_root


def kruskal():
    global parants, graph, nodes, edges
    answer = 0
    edge_count = 0
    while graph:
        if edge_count == edges:
            return answer
        cur_edge = graph.pop(0)
        if(find(cur_edge[1]) != find(cur_edge[2])):
            union(cur_edge[1], cur_edge[2])
            answer+= cur_edge[0]
            edge_count+=1
    return answer

answer = kruskal()
print(answer)
