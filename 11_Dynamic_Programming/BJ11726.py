k=int(input())
dp=[0 for i in range(k+1)]
if k==1:
    print(1)
elif k==2:
    print(2)
else:
    dp[1] =1
    dp[2] = 2
    for i in range(3, k+1):
        dp[i] = (dp[i-1]+dp[i-2])%10007
    print(dp[k])
    

