import sys
target, town_count=map(int, sys.stdin.readline().split())
town_cost=[]
for i in range(town_count):
    town_cost.append(list(map(int, sys.stdin.readline().split())))


cost_per_person=[100001 for i in range(2001)]
cost_per_person[0]=0
for cost, person in town_cost:
    for j in range(len(cost_per_person)):
        if cost_per_person[j] == 100001 : continue
        for k in range(len(cost_per_person)):
            next_cost = cost_per_person[j] + cost*k
            next_person = j + person*k
            if next_person > 2000:
                break
            else:
                cost_per_person[next_person] = min(cost_per_person[next_person], next_cost)


solution=100001
for i in range(target, len(cost_per_person)):
    solution = min(solution, cost_per_person[i])

print(solution)