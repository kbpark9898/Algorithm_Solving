#greedy + two pointer

k=int(input())
sonsil = list(map(int, input().split()))
sonsil.sort()

result=0
if k>1:
    if k%2==0:
        left = 0
        right = k-1
        for i in range((k-1)//2+1):
            result = max(result, sonsil[left] +sonsil[right])
            left+=1
            right-=1
    else:
        left = 0
        right = k-2
        for i in range((k-2)//2):
            result = max(result, sonsil[left]+sonsil[right])
            left += 1
            right -= 1
        result = max(result, sonsil[k-1])
else:
    result = sonsil[0]

print(result)