user, friendship = map(int ,input().split())
adj=[[0 for i in range(user+1)] for i in range(user+1)]
for i in range(friendship):
    source, dst = map(int, input().split())
    adj[source][dst]=1
    adj[dst][source]=1


kevin_max=10000
visited=[[kevin_max for i in range(user+1)] for i in range(user+1)]
for i in range(user+1):
    for j in range(user+1):
        if i==j:
            visited[i][j] =0

def floyd_warshal(adj, visited):
    global user
    for k in range(1, user+1):
        for i in range(1, user+1):
            for j in range(1, user+1):
                if i!=j:
                    if adj[i][k]>=1 and adj[k][j] >=1:
                        if adj[i][j] ==0:
                            adj[i][j] = adj[i][k]+adj[k][j]
                        else:
                            adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])
                        

result=[0 for i in range(user+1)]

floyd_warshal(adj, visited)

for i in range(1, user+1):
    result[i] = sum(adj[i])

result[0]=kevin_max
solution = result.index(min(result[1:-1]))
print(solution)


        



