import heapq
import sys
max_h = []
heapq.heapify(max_h)
# input()으로 입력받게되면 시간초과!
k=int(sys.stdin.readline().strip())
for i in range(k):
    command = int(sys.stdin.readline().strip())
    if command==0:
        if len(max_h)==0:
            print(0)
        else:
            print(-(heapq.heappop(max_h)))
    else:
        heapq.heappush(max_h, -command)
