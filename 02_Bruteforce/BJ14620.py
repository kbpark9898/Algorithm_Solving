from itertools import combinations
k=int(input())
hwadan=[]
for i in range(k):
    hwadan.append(list(map(int, input().split())))

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def check(cord_list):
    global k
    global dx, dy
    first_flower_cord=[cord_list[0]]
    second_flower_cord=[cord_list[1]]
    third_flower_cord=[cord_list[2]]
    flower_cord = [first_flower_cord, second_flower_cord, third_flower_cord]
    for i in range(3):
        for j in range(4):
            X = cord_list[i][0] + dx[j]
            Y = cord_list[i][1] + dy[j]
            if not(0<=X<k and 0<=Y<k):
                return False
            else:
                flower_cord[i].append([X,Y])
    for i in range(3):
        for j in range(3):
            if i!=j:
                for cord in flower_cord[i]:
                    if cord in flower_cord[j]:
                        return False
    return True
def make_price(flower_cord):
    global hwadan
    global dx, dy
    price=0
    for i in flower_cord:
        price+=hwadan[i[0]][i[1]]
        for j in range(4):
            X = i[0] + dx[j]
            Y = i[1] + dy[j]
            price+=hwadan[X][Y]
    return price


solution=5000
for i in combinations(range(k*k), 3):
    first_flower = [i[0]//k, i[0]%k]
    second_flower = [i[1]//k, i[1]%k]
    third_flower = [i[2]//k, i[2]%k]
    flower_cord=[first_flower, second_flower, third_flower]
    result = check(flower_cord)
    if result:
        current_price = make_price(flower_cord)
        solution = min(solution, current_price)

print(solution)