k = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

result = 0
for i in range(k-2):
    left = i+1
    right = k-1
    target = numbers[i]
    temp_right=k
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if target + current_sum < 0 :
            left+=1
        elif target + current_sum > 0:
            right-=1
        else:
            if numbers[left] == numbers[right]:
                result += right-left
                left+=1
            else:
                #중복 탐색을 제거하여 시간초과를 피하기 위해 해당 if문이 필요하다.
                if temp_right>right:
                    temp_right = right
                    while numbers[temp_right-1]==numbers[right]:
                        temp_right-=1
                result += right-temp_right+1
                left+=1
            
print(result)