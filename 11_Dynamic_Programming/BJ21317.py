k = int(input())
energy=[]
for i in range(k-1):
    energy.append(list(map(int, input().split())))
super_jump = int(input())
dp=[[4000000,4000000] for i in range(k+4)]
dp[0][0] = dp[0][1] = 0
for i in range(k-1):
    for j in range(2):
        dp[i+1][j]=min(dp[i][j]+energy[i][0], dp[i+1][j])
        dp[i+2][j]=min(dp[i][j]+energy[i][1], dp[i+2][j])
    dp[i+3][1] = min(dp[i+3][1], dp[i][0]+super_jump)

print(min(dp[k-1]))



