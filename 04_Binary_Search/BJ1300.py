n=int(input())
k=int(input())

def calculate(mid):
    count=0
    for i in range(1, n+1):
        count+=min(mid//i, n)
    return count

def p_search(bound, target):
    left = 1
    right = bound*bound
    while left<=right:
        mid=(left+right)//2
        # 조건문의 경계값을 > 와 <=로 바꾸면 틀림. 왜??
        if calculate(mid)>=target:
            right = mid-1
        elif calculate(mid)<target:
            left=mid+1
    return left

print(p_search(n, k))