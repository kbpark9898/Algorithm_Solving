n, k = map(int, input().split())

N = n//2

left = 0
right = N

def check(garo, target):
    global n,  k
    sero = n-garo
    if (sero+1)*(garo+1)== target:
        return True
    elif (sero+1)*(garo+1) > target:
        return 2
    else:
        return -1
    
def p_search(left, right):
    global N, k
    while left<=right:
        mid = (left+right)//2
        result = check(mid,k)
        if result == True:
            return 'YES'
        elif result == 2:
            right = mid-1
        else:
            left = mid+1
            
            
    return 'NO'

print(p_search(left, right))