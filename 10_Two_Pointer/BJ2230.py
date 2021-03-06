k, target = map(int, input().split())
numbers=[]
for i in range(k):
    numbers.append(int(input()))

numbers.sort()
left=0
right=1
#경계값 철저히 확인해서 최대 범위를 잘 설정할것!
value=3000000001

while right < k:
    gap=numbers[right]-numbers[left]
    if gap == target:
        value = gap
        break
    elif gap > target:
        value = min(gap, value)
        left+=1
    else:
        right+=1
        if right>=len(numbers):
            break
    

print(value)
