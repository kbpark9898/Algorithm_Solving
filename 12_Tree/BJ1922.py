computers = int(input())
edges = int(input())

graphs=[]
parents=[i for i in range(computers+1)]
for i in range(edges):
    src, dst, cost = map(int, input().split())
    graphs.append([cost, dst, src])

graphs.sort()



def union(a, b):
    global parents
    root_a = find(a)
    root_b = find(b)
    parents[root_b] = root_a

def find(a):
    global parents
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

edge_count = 0
def kruskal():
    global graphs, parents, computers, edges, edge_count
    result = 0
    while graphs and edge_count<computers:
        cur_edge = graphs.pop(0)
        cost, src, dst = cur_edge
        if(find(src) != find(dst)):
            union(src, dst)
            edge_count+=1
            result+=cost
    return result

answer = kruskal()
print(answer)
