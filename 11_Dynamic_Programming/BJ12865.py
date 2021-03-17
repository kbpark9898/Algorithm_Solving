stuff_count, limit = map(int, input().split())

dp=[[0 for i in range(limit+1)] for i in range(stuff_count +1)]

things=[[0,0]]

for i in range(stuff_count):
    things.append(list(map(int, input().split())))


for i in range(1, stuff_count+1):
    for j in range(1, limit+1):
        w = things[i][0]
        p = things[i][1]
        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], p + dp[i-1][j-w])

print(dp[stuff_count][limit])