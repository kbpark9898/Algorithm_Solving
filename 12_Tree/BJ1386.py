#kruskal algorithm

import sys
sys.setrecursionlimit(100000)
non_gaesu = int(input())

adj=[]

for i in range(non_gaesu):
    cur_umul = int(input())
    adj.append([cur_umul, 0, i+1])

for i in range(non_gaesu):
    cur_list = list(map(int, input().split()))
    for j in range(non_gaesu):
        if i<j:
            adj.append([cur_list[j], i+1, j+1])

adj.sort()

parents=[i for i in range(non_gaesu+1)]

def find(node):
    global parents
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(a, b):
    global parents
    parent_a = find(a)
    parent_b = find(b)
    parents[parent_b] = parent_a

solution=0
mst=[]
edge=0
while 1:
    if edge == non_gaesu:
        break
    cur_edge = adj.pop(0)
    if find(cur_edge[1]) != find(cur_edge[2]):
        union(cur_edge[1], cur_edge[2])
        solution+=cur_edge[0]
        edge+=1


print(solution)

