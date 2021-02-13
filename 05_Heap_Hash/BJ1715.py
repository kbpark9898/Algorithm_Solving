import heapq

min_h=[]
heapq.heapify(min_h)


k=int(input())
for i in range(k):
    card=int(input())
    heapq.heappush(min_h, card)
    
result=0
while len(min_h)>1:
    first_card = heapq.heappop(min_h)
    second_card = heapq.heappop(min_h)
    heapq.heappush(min_h, first_card+second_card)
    result += first_card+second_card

print(result)