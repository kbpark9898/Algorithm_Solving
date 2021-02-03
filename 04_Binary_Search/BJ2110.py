import sys
house, ap = map(int, sys.stdin.readline().split())
cordinate=[]
for i in range(house):
    cordinate.append(int(input()))

cordinate.sort()

def calculate(data, mid, bound):
    index=1
    before_cordinate=data[0]
    ap_count=1
    while index<len(data):
        if data[index]-before_cordinate < mid:
            index+=1
        else:
            before_cordinate=data[index]
            index+=1
            ap_count+=1
    if ap_count<bound:
        return False
    else:
        return True

def p_search(data, bound):
    left=0
    right=1000000000
    while left<=right:
        mid=(left+right)//2
        if calculate(data, mid, bound):
            left=mid+1
        else:
            right = mid-1
    return (left+right)//2

print(p_search(cordinate, ap))

