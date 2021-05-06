target=int(input())
left = 1
right = 1
answer = []

while 1:
    G = right**2 - left**2
    if G>=target and (right-left)==1:
        if G == target:
            answer.append(right)
        break
    if G<target:
        right+=1
    elif G>target:
        left+=1
    else:
        answer.append(right)
        left+=1
    

if answer:
    for i in answer:
        print(i)
else:
    print(-1)
