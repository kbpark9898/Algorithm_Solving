#어쩌다보니 dp...
#BFS도 가능할것 같은데..??
start = int(input())
dp=[0 for i in range(start+1)]
for i in range(2, start+1):
    dp[i] = dp[i-1]+1
    if i%3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 ==0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[start])