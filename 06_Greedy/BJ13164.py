n, groups = map(int, input().split())
line = list(map(int, input().split()))
delta=[]
for i in range(1, n):
    delta.append(line[i]-line[i-1])

delta.sort(reverse = True)

solution=0

for i in range(groups-1, n-1):
    solution+=delta[i]
print(solution)

