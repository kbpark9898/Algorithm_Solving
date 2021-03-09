# 신장 트리의 특성 이용

testcase=int(input())
answer=[]
for i in range(testcase):
    nations, flight = map(int, input().split())
    answer.append(nations-1)
    for j in range(flight):
        source, dst = map(int, input().split())

for i in range(testcase):
    print(answer[i])
