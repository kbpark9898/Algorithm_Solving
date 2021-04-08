k = int(input())
n = int(input())

sensors = list(map(int, input().split()))
sensors.sort()

gap=[]

for i in range(1, k):
    gap.append(sensors[i] - sensors[i-1])

gap.sort(reverse=True)

solution=0
for i in range(n-1, len(gap)):
    solution+=gap[i]

print(solution)