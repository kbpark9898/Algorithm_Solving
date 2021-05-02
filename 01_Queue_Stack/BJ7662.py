import heapq

n = int(input())
result=[]
for step in range(n):
    max_h =[]
    min_h = []
    heapq.heapify(max_h)
    heapq.heapify(min_h)
    k = int(input())
    id_=0
    deleted_hash={}
    for sub_step in range(k):
        flag, number = input().split()
        if flag == 'I':
            number=int(number)
            heapq.heappush(min_h, (number, id_))
            heapq.heappush(max_h, (-number, id_))
            id_+=1
        else:
            if number=='1':
                while max_h:
                    if max_h[0][1] in deleted_hash:
                        heapq.heappop(max_h)
                    else:
                        break
                if max_h:
                    deleted = heapq.heappop(max_h)
                    deleted_hash[deleted[1]] = 1
            else:
                while min_h:  
                    if min_h[0][1] in deleted_hash:
                        heapq.heappop(min_h)
                    else:
                        break
                if min_h:
                    deleted = heapq.heappop(min_h)
                    deleted_hash[deleted[1]] = 1
                      
    current_result=[]
    while max_h:
        current_max = heapq.heappop(max_h)
        if current_max[1] in deleted_hash:
            continue
        else:
            current_result.append(-current_max[0])
            break
    while min_h:
        current_min = heapq.heappop(min_h)
        if current_min[1] in deleted_hash:
            continue
        else:
            current_result.append(current_min[0])
            break
    if len(current_result)==2:
        result.append(current_result)
    else:
        result.append('EMPTY')

for i in result:
    if i == "EMPTY":
        print("EMPTY")
    else:
        print(i[0], i[1])



    


