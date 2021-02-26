k=int(input())
dp=[0 for i in range(k+1)]

if k==0:
    print(0)
elif k==1:
    print(1)
else:
    dp[0]=0
    dp[1]=1
    for i in range(2, k+1):
        dp[i] = (dp[i-1] + dp[i-2])%1000000007
    print(dp[k])

