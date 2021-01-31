import sys
#딕셔너리 이용한 풀이
k = int(input())
a=[]
b=[]
c=[]
d=[]

for i in range(k):
    q, w, e, r=map(int, sys.stdin.readline().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)


sum_dict={}
count=0
for i in a:
    for j in b:
        try:
            sum_dict[i+j]+=1
        except:
            sum_dict[i+j]=1

for i in c:
    for j in d:
        try:
            count+=sum_dict[-(i+j)]
        except:
            continue

print(count)


