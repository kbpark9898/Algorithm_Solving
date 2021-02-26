k=int(input())
num_list=list(map(int, input().split()))
dp=[1 for i in range(k+1)]


for i in range(k):
    for j in range(i):
        if num_list[i]>num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))