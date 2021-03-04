k = int(input())
triangle=[]
for i in range(k):
    triangle.append(list(map(int, input().split())))
    
dp=[]
for i in range(k):
    dp.append([0 for j in range(i+1)])

dp[0][0]=triangle[0][0]
for i in range(1, k):
    for j in range(i+1):
        if 0<j<i:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+triangle[i][j], dp[i-1][j-1]+triangle[i][j])
        elif j==0:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+triangle[i][j])
        elif j==i:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+triangle[i][j])

answer=max(dp[k-1])

print(answer)

