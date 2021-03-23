town_count=int(input())
bus_count=int(input())
max_num=100000000
metro=[[max_num for i in range(town_count+1)] for i in range(town_count+1)]

for i in range(bus_count):
    source, dst, cost = map(int, input().split())
    metro[source][dst]=min(metro[source][dst], cost)

for i in range(1, town_count+1):
    for j in range(1, town_count+1):
        if i==j:
            metro[i][j]=0

def floyd_warshall(length, adj):
    for k in range(1, length+1):
        for i in range(1, length+1):
            for j in range(1, length+1):
                if adj[i][j] > adj[i][k]+adj[k][j]:
                    adj[i][j] = adj[i][k] + adj[k][j]

floyd_warshall(town_count, metro)

for i in range(1, town_count+1):
    for j in range(1, town_count+1):
        if metro[i][j] == max_num:
            print(0, end=' ')
        else:
            print(metro[i][j], end=' ')
    print()