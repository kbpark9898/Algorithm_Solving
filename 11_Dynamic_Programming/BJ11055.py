from copy import deepcopy
length = int(input())
numbers=list(map(int, input().split()))
dp=deepcopy(numbers)
for i in range(length):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+numbers[i])
result = max(dp)


print(result)