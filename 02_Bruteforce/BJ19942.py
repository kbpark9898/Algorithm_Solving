from itertools import combinations

n = int(input())
minimum = list(map(int ,input().split()))
food=[]
for i in range(n):
    cur_food = list(map(int, input().split()))
    food.append(cur_food)

result_cost = 1000000
answers=[]
for i in range(n, 0, -1):
    for comb in combinations(range(n), i):
        cur_p, cur_f, cur_s, cur_v , cur_cost= 0,0,0,0,0
        for item in comb:
            cur_p+=food[item][0]
            cur_f+=food[item][1]
            cur_s+=food[item][2]
            cur_v+=food[item][3]
            cur_cost+=food[item][4]
        if cur_p>=minimum[0] and cur_f>=minimum[1] and cur_s>=minimum[2] and cur_v>=minimum[3]:
            if result_cost > cur_cost:
                result_cost = cur_cost
                answers=[]
                answers.append(list(comb))
            elif result_cost == cur_cost:
                answers.append(list(comb))

if result_cost == 1000000:
    print(-1)
else:
    answers.sort()
    answer = answers[0]
    for i in range(len(answer)):
        answer[i] = str(answer[i]+1)
    print(result_cost)
    print(' '.join(answer))
        

