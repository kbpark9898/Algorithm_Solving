k= int(input())
cost=[]
for i in range(k):
    cost.append(list(map(int, input().split())))

dp=[[0 for i in range(3)] for i in range(k+1)]

for i in range(3):
    dp[0][i] = cost[0][i]

for i in range(1, k):
    for j in range(3):
        if j==0:
            dp[i][j] = min(dp[i-1][1]+cost[i][j], dp[i-1][2]+cost[i][j])
        elif j==1:
            dp[i][j] = min(dp[i-1][0]+cost[i][j], dp[i-1][2]+cost[i][j])
        else:
            dp[i][j] = min(dp[i-1][0]+cost[i][j], dp[i-1][1]+cost[i][j])

answer = min(dp[k-1][0], dp[k-1][1], dp[k-1][2])

print(answer)
