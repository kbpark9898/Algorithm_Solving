k=int(input())
dp=[0 for i in range(k+1)]
dp[0]=1
dp[1]=1
for i in range(2, k+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[k])

# import sys 
# input = sys.stdin.readline 
# n = int(input()) 
# dp = [0] * 1000001 
# dp[1] = 1 
# dp[2] = 2 
# for k in range(3,n+1): 
#     dp[k] = (dp[k-1]+ dp[k-2])%15746 
# print(dp[n])

