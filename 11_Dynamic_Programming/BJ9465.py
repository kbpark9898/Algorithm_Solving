testcase=int(input())


def memoization(stickers, count, dp):
    
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    for i in range(1, count):
        if i==1:
            dp[0][1] = stickers[0][1] + dp[1][0]
            dp[1][1] = stickers[1][1] + dp[0][0]
        else:
            dp[0][i] = max(dp[1][i-1]+stickers[0][i], dp[1][i-2]+stickers[0][i])
            dp[1][i] = max(dp[0][i-1]+stickers[1][i], dp[0][i-2]+stickers[1][i])

for i in range(testcase):
    sticker_count = int(input())
    first_line = list(map(int, input().split()))
    second_line = list(map(int, input().split()))
    sticker=[]
    sticker.append(first_line)
    sticker.append(second_line)
    dp=[[0 for i in range(sticker_count)]for i in range(2)]
    memoization(sticker, sticker_count, dp)
    print(max(dp[0][sticker_count-1], dp[1][sticker_count-1]))