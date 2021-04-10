k= int(input())
ballon = list(map(int, input().split()))
#deque로 풀수 있다고 하나, 모듈로 연산 구현으로 풀었음

ballon_count = k
index=0
data = ballon.pop(index)
index_match = [i for i in range(1, k+1)]
solution=[]
solution.append(index_match.pop(index))
while ballon:
    if data>0:
        index = (index+data-1)%len(ballon)
        data=ballon.pop(index)
        solution.append(index_match.pop(index))
    else:
        index = (index+data)%len(ballon)
        data=ballon.pop(index)
        solution.append(index_match.pop(index))

for i in solution:
    print(i, end=' ')