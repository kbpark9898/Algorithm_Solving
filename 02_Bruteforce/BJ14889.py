from itertools import combinations, permutations
from copy import deepcopy

def sub_list(a, b):
    data = deepcopy(a)
    for i in b:
        idx = data.index(i)
        del data[idx]
    return data


k = int(input())
member=[i+1 for i in range(k)]
team_stat=[]
for i in range(k):
    data = list(map(int, input().split()))
    team_stat.append(data)

team_combination=[]
for i in combinations(member, k//2):
    team_combination.append(list(i))

solution_stat=1000000000
for i in range(len(team_combination)//2):
    cur_team1 = team_combination[i]
    cur_team2 = sub_list(member, cur_team1)
    stat_team1=0
    stat_team2=0

    for perm in permutations(cur_team1, 2):
        data=list(perm)
        stat_team1+=team_stat[data[0]-1][data[1]-1]
    
    for perm in permutations(cur_team2, 2):
        data=list(perm)
        stat_team2+=team_stat[data[0]-1][data[1]-1]
    cur_sub=abs(stat_team1 - stat_team2)
    solution_stat = min(solution_stat, cur_sub)

print(solution_stat)