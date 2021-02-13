import heapq
# 실패 : max heap 과 min heap의 정확한 동기화 실패.
# 특정 key 값을 이용해 해당 값이 min 또는 max heap에서 이미 pop 된 값인지 확인하는 과정이 필요
# 이걸 어떻게 풀어낼것인가..??
q_count=int(input())
bound=2**32
solution=[]
poped=[0]*bound
for i in range(q_count):
    cal_count=int(input())
    min_h=[]
    max_h=[]
    heapq.heapify(min_h)
    heapq.heapify(max_h)
    len_count=0
    for j in range(cal_count):
        calc, num = map(str, input().split())
        num=int(num)
        if calc == "I":
            heapq.heappush(min_h, num)
            heapq.heappush(max_h, -num)
            if poped[num]==1:
                poped[num]=0
            len_count+=1
        else:
            if num==1:
                if(len_count<=0):
                    pass
                else:
                    cur_num=heapq.heappop(max_h)
                    while poped[cur_num] !=1:
                        cur_num=heapq.heappop(max_h)
                    len_count-=1
                    poped[cur_num]=1
                    if len_count==0:
                        min_h=[]
                        max_h=[]
            else:
                if(len_count<=0):
                    pass
                else:
                    cur_num=heapq.heappop(min_h)
                    while poped[cur_num] !=1:
                        cur_num=heapq.heappop(min_h)
                    len_count-=1
                    poped[cur_num]=1
                    if len_count==0:
                        min_h=[]
                        max_h=[]
    if len_count<=0:
        solution.append("EMPTY")
    else:
        solution_string= str(-heapq.heappop(max_h)) + " " + str(heapq.heappop(min_h))
        solution.append(solution_string)

for i in solution:
    print(i)



