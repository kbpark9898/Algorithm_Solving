k, final=map(int, input().split())
lan_size=[]
for i in range(k):
    lan_size.append(int(input()))

lan_size.sort()
def slice_result(cables, current_mid):
    result=0
    if current_mid>0:
        for i in cables:
            result+=i//current_mid
    return result
def paramitive_search(cables, target):
    left = 0
    right = cables[len(cables)-1]
    while left<=right:
        mid=(left+right)//2
        # print(mid, slice_result(lan_size, mid), target)
        if slice_result(lan_size, mid)>=target:
            left=mid+1
        else:
            right = mid-1
    return abs((left+right)//2)

solution = paramitive_search(lan_size, final)
print(solution)

