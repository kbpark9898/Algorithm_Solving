n = int(input())

fluid = list(map(int, input().split()))

left = 0
right = n-1

result = 200000001
while left<right:
    cur_result = (fluid[left] + fluid[right])
    abs_cur_result = abs(cur_result)
    if abs(result) > abs_cur_result:
        result = cur_result
    if cur_result<0:
        left+=1
    elif cur_result>0:
        right-=1
    else:
        result = 0
        break

print(result)
