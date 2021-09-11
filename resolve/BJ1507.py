n=int(input())

graph=[]
for i in range(n):
    cur_list = list(map(int, input().split()))
    graph.append(cur_list)


route_graph=[[True for i in range(n)] for i in range(n)]

def f_w():
    global graph, route_graph, n
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not(i==k or i==j or k==j):
                    if(graph[i][j] == graph[i][k] + graph[k][j]):
                        route_graph[i][j] = False
                    elif(graph[i][j] > graph[i][k] + graph[k][j]):
                        return False
    return True

result = f_w()
answer = 0

if result:
    for i in range(n):
        for j in range(n):
            if(route_graph[i][j] == True):
                answer+=graph[i][j]
else:
    answer = -1

print(answer//2)