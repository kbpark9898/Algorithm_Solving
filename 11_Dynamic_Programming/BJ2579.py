k = int(input())
floor=[ 0 for i in range(301)]
for i in range(k):
    floor[i]=int(input())

dp=[0 for i in range(301)]


dp[0] = floor[0]
dp[1] = floor[1] + floor[0]
dp[2] = max(floor[0]+floor[2], floor[1]+floor[2])
for i in range(3, k):
    dp[i] = max(dp[i-2]+floor[i], dp[i-3]+floor[i-1]+floor[i])

print(dp[k-1])
