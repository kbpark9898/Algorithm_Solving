n, m, k = map(int, input().split())
oranges=[0 for i in range(n+1)]
dp=[0 for i in range(n+1)]
for i in range(1, n+1):
    oranges[i] = int(input())

for i in range(0, n+1):
    dp[i] = k*i

oranges[0] = oranges[1]
for i in range(n):
    min_orange = oranges[i+1]
    max_orange = oranges[i+1]
    for j in range(1, m+1): 
        if i+j <=n:
            #시간초과를 줄이기 위해 oranges[i+1:i+j+1]에서 min 혹은 max값을 구하지 않고, 하나씩 비교해서 최소 최대를 갱신함
            min_orange = min(min_orange, oranges[i+j])
            max_orange = max(max_orange, oranges[i+j])
            dp[i+j] = min(dp[i+j], dp[i] + k+j * (max_orange-min_orange))
print(dp[n])