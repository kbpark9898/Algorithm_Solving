n = int(input())
left = 0
right = n-1
number = list(map(int, input().split()))
number.sort()
target=int(input())
answer=0
while left<right:
    plus = number[left] + number[right]
    if plus>target:
        right-=1
    elif plus<target:
        left+=1
    else:
        answer+=1
        left+=1


print(answer)

    