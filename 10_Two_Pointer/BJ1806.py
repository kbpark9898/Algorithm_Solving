length, target = map(int, input().split())
numbers = list(map(int, input().split()))

left=0
right=0

sum_list=[numbers[0]]

answer=100000
for i in range(1, len(numbers)):
    sum_list.append(sum_list[i-1]+numbers[i])

while right<length:
    if sum_list[right]- sum_list[left]>=target:
        answer = min(answer, right-left)
        left+=1
    else:
        right+=1
if sum_list[right-1]==target:
    answer = length

if answer==100000:
    answer = 0

print(answer)