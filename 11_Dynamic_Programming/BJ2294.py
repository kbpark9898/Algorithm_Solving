n, k=map(int, input().split())
coins=[]

for i in range(n):
    coins.append(int(input()))

coins.sort()
dp=[10001 for i in range(k+1)]
dp[0]=0

for coin in coins:
    for j in range(coin, k+1):
        dp[j] = min(dp[j], dp[j-coin]+1)

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])