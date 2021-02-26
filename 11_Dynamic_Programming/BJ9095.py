k=int(input())
result=[]
for i in range(k):
    size = int(input())
    dp=[0 for num in range(size+1)]
    if size==1:
        result.append(1)
        continue
    elif size==2:
        result.append(2)
    elif size==3:
        result.append(4)
    else:
        dp[1]=1
        dp[2]=2
        dp[3]=4
        for j in range(4, size+1):
            dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
        result.append(dp[size])

for i in range(k):
    print(result[i])