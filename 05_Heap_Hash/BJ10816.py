k=int(input())
number_list = list(map(int, input().split()))
h={}
for i in number_list:
    if i in h:
        h[i]+=1
    else:
        h[i]=1

k=int(input())
number_list = list(map(int, input().split()))

for i in number_list:
    if i in h:
        print(h[i], end=' ')
    else:
        print(0, end=' ')