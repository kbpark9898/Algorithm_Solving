#dfs 이용한 풀이 실패. 왜?
n=-1
e=-1
adj=[]
adj_index=0
is_zero=False
while n!=0 and e!=0:
    n, e = map(int, input().split())
    if n==0 and e==0 and adj_index==0:
        is_zero=True
        break
    adj.append([[] for i in range(n+1)])
    for i in range(e):
        start, end = map(int, input().split())
        adj[adj_index][start].append(end)
        adj[adj_index][end].append(start)
    adj_index+=1
visited=[[0 for i in range(500)] for j in range(adj_index)]


answer=[0 for i in range(adj_index)]

def dfs(visit, start, adj, before_node):
    visit[start] = 1

    for i in adj[start]:
        if i == before_node:
            continue
        if visit[i] == 1:
            return False
        if dfs(visit, i, adj, start)==False:
            return False
    return True

if not is_zero:
    for i in range(0, len(adj)):
        current_answer=0
        for j in range(1, len(adj[i])):
            if visited[i][j] ==0:
                if dfs(visited[i], j, adj[i], 0) == True:
                    current_answer+=1
        answer[i] = current_answer


    for i in range(len(answer)-1):
        if answer[i] >1:
            print("Case %d: A forest of %d trees." %(i+1, answer[i]))
        elif answer[i] ==1 :
            print("Case %d: There is one tree."%(i+1))
        else:
            print("Case %d: No trees." % (i+1))
    