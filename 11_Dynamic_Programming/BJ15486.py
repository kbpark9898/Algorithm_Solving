k = int(input())

table=[]
dp=[]
for i in range(k):
    current_input=list(map(int, input().split()))
    table.append(current_input)
    dp.append(current_input[1])

dp.append(0)
for i in range(k-1, -1, -1):
    if i+table[i][0] > k:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i] + dp[i+table[i][0]])

print(dp[0])