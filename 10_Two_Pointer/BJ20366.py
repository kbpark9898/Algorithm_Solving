from itertools import combinations

k = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

result =2000000000
for i in range(k):
    for j in range(i+3, k):
        elsa = numbers[j]+numbers[i]
        left = i+1
        right = j-1
        while left<right:
            anna = numbers[left] + numbers[right]
            height_gap = elsa - anna
            result = min(result, abs(height_gap))
            if height_gap<0:
                right-=1
            else:
                left+=1
     

print(result)

