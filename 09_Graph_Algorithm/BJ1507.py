n = int(input())

graph=[]

for i in range(n):
    cur_list = list(map(int, input().split()))
    graph.append(cur_list)

new_graph=[[True for i in range(n)] for j in range(n)]

def f_w(graph):
    global n
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not(i==j or i==k or k==j ):
                    if graph[i][j] == graph[i][k] + graph[k][j]:
                        new_graph[i][j] = False
                    elif graph[i][j] > graph[i][k] + graph[k][j]:
                        return False
    return True
                    

result = f_w(graph)

if result:
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            if new_graph[i][j]:
                result+= graph[i][j]
else:
    result = -1

print(result)