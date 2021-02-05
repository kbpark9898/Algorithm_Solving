import heapq
import sys

k=int(input())
data=[]
heapq.heapify(data)
for i in range(k):
    input_data = list(map(int, sys.stdin.readline().split()))
    if len(data)==0:
        for j in input_data:
            heapq.heappush(data, j)
    else:
        current_smallest = heapq.nsmallest(1, data)
        for j in input_data:
            if j > current_smallest[0]:
                heapq.heappushpop(data, j)

big_el=heapq.nlargest(k, data)
print(big_el[k-1])