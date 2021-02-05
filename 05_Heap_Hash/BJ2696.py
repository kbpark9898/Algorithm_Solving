import heapq
import sys
k=int(input())
midvalues=[]
for i in range(k):
    current_length=int(input())
    data=[]
    heapq.heapify(data)
    current_midvalues=[]
    if current_length<10:
        line=list(map(int, sys.stdin.readline().split()))
        for j in range(len(line)):
            heapq.heappush(data, line[j])
            if (j+1)%2 !=0:
                left_of_heap=heapq.nsmallest(len(data)//2+1, data)
                current_midvalues.append(left_of_heap[(len(data)//2)])
        midvalues.append(current_midvalues)
    else:
        if current_length%10 ==0:
            for j in range(current_length//10):
                line=list(map(int, sys.stdin.readline().split()))
                for k in range(len(line)):
                    heapq.heappush(data, line[k])
                    if(k+1)%2 !=0:
                        left_of_heap=heapq.nsmallest(len(data)//2+1, data)
                        current_midvalues.append(left_of_heap[(len(data)//2)])
            midvalues.append(current_midvalues)
        else:
            for j in range(current_length//10+1):
                line=list(map(int, sys.stdin.readline().split()))
                for k in range(len(line)):
                    heapq.heappush(data, line[k])
                    if(k+1)%2 !=0:
                        left_of_heap=heapq.nsmallest(len(data)//2+1, data)
                        current_midvalues.append(left_of_heap[(len(data)//2)])
            midvalues.append(current_midvalues)

for i in range(len(midvalues)):
    print(len(midvalues[i]))
    for j in range(len(midvalues[i])):
        if j%10==0 and j!=0:
            print(midvalues[i][j])
        else:
            print(midvalues[i][j], end=' ')
    print()


