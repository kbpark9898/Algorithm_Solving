current_store, new_store, length = map(int, input().split())
cord=[0]
cord = cord + list(map(int, input().split()))
cord.append(length)
cord.sort()
def check(cord, new_store, target, length):
    available=0
    for i in range(1, len(cord)):
        available += (cord[i] - cord[i-1]-1)//target
    if available>new_store:
        return True
    else:
        return False

left = 1
right = length-1
def p_search(cord, new_store, left, right, length):
    while left <= right:
        mid = (left+right)//2
        if check(cord, new_store, mid, length):
            left= mid+1
        else:
            right = mid-1
    return left

result = p_search(cord, new_store, left, right, length)
print(result)
    