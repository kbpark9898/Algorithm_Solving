k=int(input())
t=[]
p=[]
dp=[]
for i in range(k):
    data=list(map(int, input().split()))
    t.append(data[0])
    p.append(data[1])
    dp.append(data[1])
dp.append(0)
for i in range(k-1, -1, -1):
    if (i+t[i])>k:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])
print(dp[0])