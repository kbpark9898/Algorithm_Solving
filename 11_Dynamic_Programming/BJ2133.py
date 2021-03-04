k=int(input())
if k%2==0:
    dp=[0 for i in range(k+1)]
    dp[2]=3

    for i in range(4, k+1):
        if i%2==0:
            double=0
            for j in range(i-3):
                double+=dp[j]
            dp[i] = 2+dp[i-2]*3+double*2

    print(dp[k])
else:
    print(0)