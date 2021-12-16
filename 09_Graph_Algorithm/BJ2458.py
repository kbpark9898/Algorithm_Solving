nodes, edges = map(int, input().split())
MAX = 10
graph=[[MAX for i in range(nodes+1)]for j in range(nodes+1)]
for i in range(edges):
    src, dst = map(int, input().split())
    graph[src][dst] = 0



def f_w():
    global nodes
    global edges
    global graph
    for k in range(1, nodes+1):
        for i in range(1, nodes+1):
            for j in range(1, nodes+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return


def play(adj, nodes):
    result = 0
    for i in range(1, nodes+1):
        is_break = False
        for j in range(1, nodes+1):
            if adj[i][j] != 0 and adj[j][i] != 0:
                if i!=j:
                    is_break = True
                    break
        if not is_break:
            result+=1
    return result

f_w()
answer = play(graph, nodes)
print(answer)

