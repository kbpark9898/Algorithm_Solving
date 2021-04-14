k = int(input())
triangle=[1]
polygon=[1]

current_t=1
current_p=1

while current_p<=k:
    current_t+=1
    triangle.append(triangle[-1]+current_t)
    polygon.append(polygon[-1]+triangle[-1])
    current_p = polygon[-1]

polygon.pop()
dp=[300001 for i in range(k+1)]
dp[0] = 0
for p in polygon:
    for j in range(p, k+1):
        dp[j] = min(dp[j] , dp[j-p]+1)

print(dp[k])




