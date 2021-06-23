#https://programmers.co.kr/learn/courses/30/lessons/42586
#	[1, 30, 5]	[2, 1]
#[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
from collections import deque
#O(N**2) 풀이
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while progresses:
        current_pop = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while progresses:
            if progresses[0] >=100:
                progresses.popleft()
                speeds.popleft()
                current_pop+=1
            else:
                break
        if current_pop != 0:
            answer.append(current_pop)
    return answer

#개선 풀이
# progress=list(map(int, input().split()))
# speeds=list(map(int, input().split()))
# solution_q=deque()
# answer_q=[]

# def make_deque(p, s):
#     global solution_q
#     for i in range(len(p)):
#         if (100-p[i])%s[i] !=0:
#             solution_q.append((100-p[i])//s[i] +1)
#         else:
#             solution_q.append((100-p[i])//s[i])
# def solution(p, s):
#     global solution_q
#     global answer_q
#     make_deque(p, s)
#     count=1
#     bound=solution_q.popleft()
#     while solution_q:
#         if bound>=solution_q[0]:
#             count+=1
#             solution_q.popleft()
#         else:
#             answer_q.append(count)
#             count=1
#             bound = solution_q.popleft()
#     answer_q.append(count)

# solution(progress, speeds)
# print(answer_q)