#https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

#SJF 스케쥴링 알고리즘
import heapq

# resolve 0911
import heapq
def solution(jobs):
    answer = 0
    now = 0
    last_started = -1
    complete_count = 0
    h= []
    while complete_count < len(jobs):
        for job in jobs:
            if(last_started < job[0] <= now):
                heapq.heappush(h, [job[1], job[0]])
        if h:
            cur_job = heapq.heappop(h)
            last_started = now
            now += cur_job[0]
            complete_count +=1
            answer += (now-cur_job[1])
        else:
            now+=1
    answer = answer // len(jobs)
    return answer
# def solution(jobs):
#     answer = 0
#     count = 0
#     last_job_started = -1
#     now = 0
#     job_h=[]

#     while count < len(jobs):
#         for job in jobs:
#             if last_job_started < job[0] <= now:
#                 heapq.heappush(job_h, [job[1], job[0]])
#         if job_h:
#             cur_job = heapq.heappop(job_h)
#             last_job_started = now
#             now+=cur_job[0]
#             answer += now-cur_job[1]
#             count+=1
#         else:
#             now+=1
#     answer = answer//len(jobs)
#     return answer

