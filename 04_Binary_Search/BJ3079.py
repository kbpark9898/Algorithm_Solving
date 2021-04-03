n, m = map(int, input().split())

immigration=[]

for i in range(n):
    immigration.append(int(input()))

left =0
right = m*(max(immigration))

def check(imm, target, n):
    result=0
    for time in imm:
        result += target // time
    if result <n:
        return False
    else:
        return True

def p_search(left, right, imm, n):
    mid=0
    while left<=right:
        mid = (left+right)//2
        if check(imm, mid ,n):
            right = mid-1
        else:
            left = mid+1
    
    return left

solution = p_search(left, right, immigration, m)
print(solution)