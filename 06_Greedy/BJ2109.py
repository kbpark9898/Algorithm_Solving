import heapq

k=int(input())
lecture=[]
for i in range(k):
    pay, day = map(int, input().split())
    lecture.append([pay, day])

lecture.sort(key=lambda lecture_data: lecture_data[1])
solution=[]
heapq.heapify(solution)
for item in lecture:
    heapq.heappush(solution, item[0])
    if len(solution)>item[1]:
        heapq.heappop(solution)

answer=0
for i in range(len(solution)):
    answer+=heapq.heappop(solution)

print(answer)