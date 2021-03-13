testcase = int(input())

result=[]
for i in range(testcase):
    dp=[0 for i in range(101)]
    dp[0] = dp[1] = dp[2] = 1
    dp[3] = dp[4] = 2
    n = int(input())
    for i in range(5, n):
        dp[i] = dp[i-1] + dp[i-5]
    result.append(dp[n-1])

for i in result:
    print(i)
    
