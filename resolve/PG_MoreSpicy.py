# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

# resolve 0911
def check(h, k):
    for item in h:
        if item <k:
            return False
    return True

def solution(scoville, K):
    answer = 0
    h = []
    for s in scoville:
        heapq.heappush(h, s)
    while len(h)>1:
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        mix = first+second*2
        heapq.heappush(h, mix)
        answer+=1
        result = check(h, K)
        if(result):
            return answer
    result = check(h, K)
    if(not result):
        return -1
    return answer