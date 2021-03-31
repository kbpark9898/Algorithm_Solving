length, limit = map(int, input().split())
numbers = list(map(int, input().split()))
h={}
first=0
second=0
solution=0
while second<length and first <=second:
    if numbers[second] in h:
        h[numbers[second]]+=1
    else:
        h[numbers[second]]=1
    if h[numbers[second]] > limit:
        while h[numbers[second]]>limit:
            before_left = numbers[first]
            first+=1
            h[before_left]-=1
        second+=1
    else:
        solution = max(solution, second - first)
        second+=1

print(solution+1)
    