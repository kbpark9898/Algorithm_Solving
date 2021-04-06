from itertools import combinations

k=int(input())
recipie = []
for i in range(k):
    recipie.append(list(map(int, input().split())))

taste=100000000
for i in range(1, k+1):
    for comb in combinations(range(k), i):
        current_taste=[recipie[comb[0]][0], recipie[comb[0]][1]]
        for j in range(1, i):
            current_taste[0] *= recipie[comb[j]][0]
            current_taste[1] += recipie[comb[j]][1]
        taste = min(taste, abs(current_taste[0] - current_taste[1]))

print(taste)
