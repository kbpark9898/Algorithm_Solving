k, target = map(int, input().split())
numbers=[]
for i in range(k):
    numbers.append(int(input()))

numbers.sort()
left=0
right=1
value=1000000001

while left<k and right<k:
    gap=numbers[right]-numbers[left]
    if gap == target:
        value = gap
        break
    elif gap > target:
        value = min(gap, value)
        left+=1
    else:
        right+=1
    

print(value)
