import heapq

k=int(input())
data=[]
for i in range(k):
    data.append(int(input()))


_list=[]
heapq.heapify(_list)
for i in data:
    if i==0:
        if len(_list)>0:
            print(heapq.heappop(_list))
        else:
            print(0)
    else:
        heapq.heappush(_list, i)

