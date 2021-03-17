import heapq
k=int(input())

h=[]
heapq.heapify(h)

for i in range(k):
    heapq.heappush(h, int(input()))


while h:
    print(heapq.heappop(h))