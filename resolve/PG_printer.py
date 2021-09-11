# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

# resolve 0911
def solution(priorities, location):
    pri = deque(priorities)
    answer = 0
    pri[location] *= -1
    while pri:
        before_len = len(pri)
        cur_print = pri.popleft()
        for i in range(len(pri)):
            if(abs(pri[i])>abs(cur_print)):
                pri.append(cur_print)
                break
        if(len(pri) != before_len):
            answer+=1
            if(cur_print < 0):
                return answer

# def solution(priorities, location):
#     answer = 1
#     prior_index=[]
#     is_printed=True
#     for i in range(len(priorities)):
#         prior_index.append([i, priorities[i]])
#     location_prior = priorities[location]
#     while 1:
#         is_printed=True
#         current = prior_index.pop(0)
#         for i in prior_index:
#             if current[1]<i[1]:
#                 prior_index.append(current)
#                 is_printed=False
#                 break
#         if is_printed:
#             if current[0]==location:
#                 return answer
#             else:
#                 answer+=1
#                 is_printed=False
        
#     return answer