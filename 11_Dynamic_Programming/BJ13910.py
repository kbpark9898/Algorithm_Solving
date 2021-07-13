from itertools import combinations

dp=[10001 for i in range(10001)]
dp[0] = 0
target, wok_num = map(int ,input().split())

woks = list(map(int, input().split()))
woks.sort()


for index in range(10001):
    for wok in woks:
        if index+wok <= 10000:
            dp[index+wok] = min(dp[index+wok], dp[index]+1)
    for comb in combinations(woks, 2):
        if index+comb[0]+comb[1] <= 10000:
            dp[index+comb[0]+comb[1]] = min(dp[index+comb[0]+comb[1]], dp[index]+1)

# print(dp[:11])
if dp[target] == 10001:
    print(-1)
else:
    print(dp[target])

