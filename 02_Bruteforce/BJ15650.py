from itertools import combinations

bound, count = map(int, input().split())
numbers = [str(i+1) for i in range(bound)]
for i in combinations(numbers, count):
    solution=list(i)
    print(' '.join(solution))