import sys
sys.setrecursionlimit(100000)

total_field = int(input())
adj=[]

for i in range(total_field):
    cost = int(input())
    adj.append([cost, 0, i+1])

for i in range(total_field):
    cur_list = list(map(int, input().split()))
    for j in range(total_field):
        if(i != j):
            adj.append([cur_list[j], i+1, j+1])


parents = [i for i in range(total_field+1)]

adj.sort()
def find(a):
    global parents
    if(a != parents[a]):
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    global parents
    a_root = find(a)
    b_root = find(b)
    parents[b_root] = a_root



def kruskal():
    global parents, total_field, adj
    edges = total_field
    edge_count = 0
    answer = 0
    while 1:
        if edge_count == edges:
            return answer
        cur_edge = adj.pop(0)
        if(find(cur_edge[1]) != find(cur_edge[2])):
            union(cur_edge[1], cur_edge[2])
            answer+=cur_edge[0]
            edge_count+=1
    return answer

result = kruskal()

print(result)

    