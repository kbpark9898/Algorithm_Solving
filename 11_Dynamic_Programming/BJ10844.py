n=int(input())
dp=[[0 for i in range(10)]for i in range(n+1)]
for i in range(1, 10):
    dp[0][i] = 1

dp[0][0]=0

for i in range(1, n+1):
    for j in range(10):
        if j==0:
            dp[i][j]=dp[i-1][1] 
        elif j==9:
            dp[i][j]=dp[i-1][8] 
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])

answer=0
for i in range(10):
    answer+=dp[n-1][i]
answer=answer% 1000000000
print(answer)
