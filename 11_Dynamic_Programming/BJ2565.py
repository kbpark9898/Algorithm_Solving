k=int(input())
lines=[]
for i in range(k):
    lines.append(list(map(int, input().split())))


lines = sorted(lines, key=lambda x: x[0])
dp=[1 for i in range(k+1)]

for i in range(k):
    for j in range(i):
        if lines[i][1]>lines[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
answer = k-max(dp)
print(answer)
