def check(wood, target):
    total_length=0
    for i in wood:
        if i>target:
            total_length+=i-target
    return total_length



n, m = map(int, input().split())
wood = list(map(int, input().split()))

def b_search(wood):
    global m
    left = 0
    right = 1000000001
    while left<=right:
        mid = (left+right)//2
        result = check(wood, mid)
        if result >= m:
            left = mid+1
        else:
            right = mid-1
    return (left+right)//2

answer = b_search(wood)

print(answer)
        