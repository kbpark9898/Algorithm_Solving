from itertools import combinations_with_replacement

bound, count = map(int, input().split())
numbers = [str(i+1) for i in range(bound)]
for i in combinations_with_replacement(numbers, count):
    solution=list(i)
    print(' '.join(solution))