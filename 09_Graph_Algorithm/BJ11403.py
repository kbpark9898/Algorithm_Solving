from collections import deque
k=int(input())
adj_metrix=[]
for i in range(k):
    current_line = list(map(int, input().split()))
    current_visit = [0 for j in range(k)]
    adj_metrix.append(current_line)
  

#플로이드-워셜 알고리즘 응용. 모든 간선에 대해서 확인한다는 아이디어를 차용함.
def floyd_warshall(length, adj):
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if adj[i][k] == adj[k][j] ==1:
                    adj[i][j] =1

floyd_warshall(k, adj_metrix)
for i in range(k):
    for j in range(k):
        print(adj_metrix[i][j], end=' ')
    print()







