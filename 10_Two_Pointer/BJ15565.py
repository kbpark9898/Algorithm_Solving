n, k= map(int, input().split())
dolls = list(map(int, input().split()))
lion_index =[]

for i in range(len(dolls)):
    if dolls[i] ==1:
        lion_index.append(i)

left=0
right=k-1
answer=1000000
while right<len(lion_index):
    answer = min(answer, lion_index[right]-lion_index[left])
    left+=1
    right+=1

if len(lion_index)<k:
    print(-1)
else:
    print(answer+1)