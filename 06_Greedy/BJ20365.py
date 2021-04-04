#그리디 보다는 그냥 문자열과 구현에 가까운 문제같은데..

k=int(input())
string = list(input())
count={'B':0, 'R':0}
before_letter = string[0]
count[string[0]]+=1
for i in range(1, k):
    if before_letter != string[i]:
        count[string[i]]+=1
        before_letter = string[i]

solution=min(count['B']+1, count['R']+1)
print(solution)
