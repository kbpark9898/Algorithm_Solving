n, k = map(int, input().split())
number = list(input())
poped_count = 0
stack=[]
length = n-k
for i in range(n):
    if not stack:
        stack.append(number[i])
    else:
        if poped_count<k:
            while stack:
                if int(stack[-1]) < int(number[i]):
                    stack.pop()
                    poped_count+=1
                    if poped_count == k:
                        break
                else:
                    break
            if len(stack) < length:
                stack.append(number[i])
        else:
            if len(stack) < length:
                stack.append(number[i])

result = ''.join(stack)
print(result)

