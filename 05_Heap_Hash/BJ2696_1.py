#통과 코드
# max heap 과 min heap을 이용해 중앙값 도출 과정에 걸리는 시간을 최소화함
import heapq
import sys
k=int(input())
midvalues=[]

def make_heap(data, min_h, max_h):
    if len(min_h)==len(max_h):
        if len(max_h)==0:
            heapq.heappush(max_h, -data)
        else:
            if min_h[0]<=data:
                mindata = -(heapq.heappop(min_h))
                heapq.heappush(max_h, mindata)
                heapq.heappush(min_h, data)
            else:
                heapq.heappush(max_h, -data)
    else:
        if -max_h[0] >data:
            maxdata = -(heapq.heappop(max_h))
            heapq.heappush(min_h, maxdata)
            heapq.heappush(max_h, -data)
        else:
            heapq.heappush(min_h, data)

            
for i in range(k):
    current_length=int(input())
    maxh=[]
    minh=[]
    current_midvalues=[]
    heapq.heapify(maxh)
    heapq.heapify(minh)
    if current_length<10:
        line=list(map(int, sys.stdin.readline().split()))
        for j in range(len(line)):
            make_heap(line[j], minh, maxh)
            if(j+1)%2:
                current_midvalues.append(-maxh[0])
        midvalues.append(current_midvalues)
    else:
        if current_length%10 ==0:
            for j in range(current_length//10):
                line=list(map(int, sys.stdin.readline().split()))
                for k in range(len(line)):
                    make_heap(line[k], minh, maxh)
                    if (k+1)%2:
                        current_midvalues.append(-maxh[0])
            midvalues.append(current_midvalues)
        else:
            for j in range(current_length//10+1):
                line=list(map(int, sys.stdin.readline().split()))
                for k in range(len(line)):
                    make_heap(line[k], minh, maxh)
                    if (k+1)%2:
                        current_midvalues.append(-maxh[0])
            midvalues.append(current_midvalues)

for i in range(len(midvalues)):
    print(len(midvalues[i]))
    for j in range(len(midvalues[i])):
        if j%10==0 and j!=0:
            print(midvalues[i][j])
        else:
            print(midvalues[i][j], end=' ')
    print()


