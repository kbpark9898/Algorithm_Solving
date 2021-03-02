n= int(input())
card_list = list(map(int, input().split()))

dp=[0 for i in range(1001)]

dp[0]=0
dp[1]=card_list[0]

for i in range(2, n+1):
    for card in range(len(card_list)):
        if i-card-1>=0:
            dp[i] = max(dp[i], dp[i-card-1]+card_list[card])

print(dp[n])
