import sys
cases = int(input())

sys.setrecursionlimit(100000)

def dfs(start):
    global n, students, cycle, visited
    visited[start] = 1
    cycle.append(start)
    next_node = students[start]
    if visited[next_node] == 0:
        dfs(next_node)
    else:
        if next_node in cycle:
            return cycle_len(cycle, next_node)

def cycle_len(cycle, node):
    global solution
    result = cycle[cycle.index(node):]
    solution+=len(result)


for i in range(cases):
    n = int(input())
    students=[0] + list(map(int, input().split()))
    
    visited=[0 for i in range(n+1)]
    solution=0
    for i in range(1, n+1):
        cycle=[]
        if visited[i] == 0:
            dfs(i)
    print(n-solution)