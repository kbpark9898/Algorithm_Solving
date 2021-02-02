import sys
n, m = map(int, sys.stdin.readline().split())
lesson=list(map(int, sys.stdin.readline().split()))



def is_correct(data, mid, bound):
    count=0
    current_sum=0
    i=0
    while i<len(data):
        if data[i]>mid:
            return True
        current_sum+=data[i]
        if current_sum>mid:
            i-=1
            current_sum=0
            count+=1
        i+=1
    if count>bound-1:
        return True
    else:
        return False

def p_search(data, bound):
    left = 0
    right = 10000*100000
    while left<=right:
        mid=(left+right)//2
        if is_correct(data, mid, bound):
            left=mid+1
        else:
            right=mid-1
    return left

print(p_search(lesson, m))
        
