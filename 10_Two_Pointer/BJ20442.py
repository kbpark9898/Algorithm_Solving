k=input()
r_count=0
result=0
left_k=[]
right_k=[]

left_count=0
for i in k:
    if i=='K':
        left_count+=1
    else:
        left_k.append(left_count)

reverse_k = k[::-1]
right_count=0
for i in reverse_k:
    if i == 'K':
        right_count+=1
    else:
        right_k.append(right_count)
right_k = right_k[::-1]

left = 0
right = len(left_k)-1

result=0
while left<=right:
    result = max(result, right-left+2*(min(left_k[left], right_k[right]))+1)
    if left_k[left] > right_k[right]:
        right -= 1
    else:
        left += 1

print(result)

