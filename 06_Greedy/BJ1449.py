# 데이터가 정렬된 채로 제공되는지, 그렇지 않은지 항상 주의하여 확인할것!

k, length = map(int, input().split())
solution=1
current_length=0
pipe=[]
pipe = list(map(int, input().split()))
pipe = sorted(pipe)
start_cordi=pipe[0]-0.5
for i in range(1, k):
    if (pipe[i]+0.5) - start_cordi >length:
        solution+=1
        start_cordi=pipe[i]-0.5

print(solution)
    