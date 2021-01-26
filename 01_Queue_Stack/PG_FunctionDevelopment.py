from collections import deque

progress=list(map(int, input().split()))
speeds=list(map(int, input().split()))
solution_q=deque()
answer_q=[]

def make_deque(p, s):
    global solution_q
    for i in range(len(p)):
        if (100-p[i])%s[i] !=0:
            solution_q.append((100-p[i])//s[i] +1)
        else:
            solution_q.append((100-p[i])//s[i])
def solution(p, s):
    global solution_q
    global answer_q
    make_deque(p, s)
    count=1
    bound=solution_q.popleft()
    while solution_q:
        if bound>=solution_q[0]:
            count+=1
            solution_q.popleft()
        else:
            answer_q.append(count)
            count=1
            bound = solution_q.popleft()
    answer_q.append(count)

solution(progress, speeds)
print(answer_q)

        
        
