from itertools import combinations

size, chicken = map(int, input().split())
jido=[]
for i in range(size):
    jido.append(list(map(int, input().split())))
chicken_list=[]
house_list=[]
combination=[]

def make_chicken_list():
    global chicken_list, size, jido
    for i in range(size):
        for j in range(size):
            if jido[i][j] == 2:
                chicken_list.append([i, j])

def make_house_list():
    global house_list, size
    for i in range(size):
        for j in range(size):
            if jido[i][j] ==1:
                house_list.append([i, j])

def make_combination():
    global chicken_list, combination
    for i in combinations([k for k in range(len(chicken_list))], chicken):
        _data=[]
        for j in range(chicken):
            _data.append(chicken_list[(i[j])])
        combination.append(_data)

def solution():
    global combination, house_list ,result
    for cur_comb in combination:
        chicken_dist = 0
        for cur_house in house_list:
            menimum_distance=1000000
            for chicken_cord in cur_comb:
                menimum_distance=min(menimum_distance, 
                (abs(cur_house[0]-chicken_cord[0])+abs(cur_house[1]-chicken_cord[1])))
            chicken_dist+=menimum_distance
        result = min(result, chicken_dist)

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
result=100000000

make_chicken_list()
make_combination()
make_house_list()
solution()
print(result)


        