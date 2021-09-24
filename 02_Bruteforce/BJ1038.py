from itertools import combinations

target = int(input())

if target > 1022:
    print(-1)
else:
    numbers = []
    for i in range(1, 11):
        for comb in combinations (['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], i):
            cur_num = int(''.join(list(comb)[::-1]))
            numbers.append(cur_num)
    numbers.sort()
    print(numbers[target])