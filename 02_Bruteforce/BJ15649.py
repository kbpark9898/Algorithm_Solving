from itertools import permutations
bound, count = map(int, input().split())
data=[str(i+1) for i in range(bound)]

for i in permutations(data, count):
    solution=list(i)
    print(' '.join(solution))