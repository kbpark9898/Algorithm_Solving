import sys
sys.setrecursionlimit(10000)
nodes, edges = map(int, input().split())

parents = [i for i in range(nodes)]

def find(a):
    global parents
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    global parents
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parents[max(root_b, root_a)] = min(root_a, root_b)
        return True
    return False


result = 0
is_break = False
for i in range(edges):
    src, dst = map(int, input().split())
    if is_break == False:
        union_result = union(src, dst)
        if union_result == False:
            result = i+1
            is_break = True

print(result)

