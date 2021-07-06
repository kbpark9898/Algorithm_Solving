n, target = map(int, input().split())

numbers = list(map(int, input().split()))




def check(numbers, mid, target):
    gugan = 1
    maximum = numbers[0]
    minimum = numbers[0]
    start_index = 0

    for i in range(len(numbers)):
        cur_gugan = numbers[start_index : i+1]
        maximum = max(cur_gugan)
        minimum = min(cur_gugan)
        if maximum-minimum > mid:
            gugan += 1
            start_index = i
        if gugan >target:
            return False
    return True
        

def p_search(numbers, target):
    left = 0
    right = 10000
    while left<=right:
        mid = (left+right) //2
        if not check(numbers, mid, target):
            left = mid +1
        else:
            right = mid -1
    return left

    
result = p_search(numbers, target)

print(result)
