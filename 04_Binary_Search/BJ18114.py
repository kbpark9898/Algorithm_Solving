#이분탐색 실패.. 왜 안될까?
#memoization으로 풀이
def p_search(left, right, target, numbers):
    while left<=right:
        mid = (left + right) //2
        if numbers[mid] <= target:
            left = mid +1
        elif numbers[mid] > target:
            right = mid-1
    return (left+right)//2


n, c = map(int, input().split())
products = list(map(int, input().split()))
products.sort()
is_possible = False
memo = [0 for i in range(100000001)]

for i in products:
    memo[i] = 1
for i in range(n):
    if is_possible:
        break
    first = products[i]
    if first == c:
        is_possible = True
        break
    for j in range(i+1, n):
        second = products[j]
        if second == c or first+second == c:
            is_possible = True
            break
        sub = c-(first+second)
        if memo[sub] == 1 and sub != first and sub != second:
            is_possible = True
            break

if is_possible:
    print(1)
else:
    print(0)


