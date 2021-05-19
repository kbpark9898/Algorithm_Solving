# 1:3, 2 3 :3/7, 4:7
from collections import deque
gears=[]
for i in range(4):
    cur_gear = deque(list(input()))
    gears.append(cur_gear)

# 반시계방향 회전
def left_shift(gear):
    first = gear.popleft()
    gear.append(first)

#시계방향 회전
def right_shift(gear):
    last = gear.pop()
    gear.appendleft(last)

#회전방향 최종 결정
def define_direction(chain_bool , direction):
    if direction == -1:
        for index in range(4):
            chain_bool[index] *= -1
#회전
def play_shift(chain_bool, gears):
    for i in range(4):
        if chain_bool[i] == 1:
            right_shift(gears[i])
        elif chain_bool[i] == -1:
            left_shift(gears[i])

# 방향결정 및 회전 호출
def play(chain_bool, direction, gears):
    define_direction(chain_bool, direction)
    play_shift(chain_bool, gears)


#연쇄반응 확인 - 비트마스크를 이용하는 방법은 없을까..?
def chain_reaction(num, direction):
    global gears
    g_idx = num-1
    chain_bool=[0,0,0,0]
    if num==1:
        chain_bool[0]=1
        if gears[g_idx][2] != gears[1][6]:
            chain_bool[1] = chain_bool[0] * -1
        if chain_bool[1] != 0 and gears[1][2] != gears[2][6]:
            chain_bool[2] = chain_bool[1] * -1
        if chain_bool[2] !=0 and gears[2][2] != gears[3][6]:
            chain_bool[3] = chain_bool[2]* -1
        play(chain_bool, direction, gears)
    elif num==2:
        chain_bool[1]=1
        if gears[g_idx][2] != gears[2][6]:
            chain_bool[2] = chain_bool[1] * -1
        if gears[g_idx][6] != gears[0][2]:
            chain_bool[0] = chain_bool[1] * -1
        if chain_bool[2] != 0 and gears[2][2] != gears[3][6]:
            chain_bool[3] = chain_bool[2] * -1
        play(chain_bool, direction, gears)
    elif num==3:
        chain_bool[2] = 1
        if gears[g_idx][2] != gears[3][6]:
            chain_bool[3] = chain_bool[2] * -1
        if gears[g_idx][6] != gears[1][2]:
            chain_bool[1] = chain_bool[2] * -1
        if chain_bool[1] != 0 and gears[1][6] != gears[0][2]:
            chain_bool[0] = chain_bool[1] * -1
        play(chain_bool, direction, gears)
    elif num==4:
        chain_bool[3] = 1
        if gears[g_idx][6] != gears[2][2]:
            chain_bool[2] = chain_bool[3] * -1
        if chain_bool[2] != 0 and gears[2][6] != gears[1][2]:
            chain_bool[1] = chain_bool[2] * -1
        if chain_bool[1] != 0 and gears[1][6] != gears[0][2]:
            chain_bool[0] = chain_bool[1] * -1
        play(chain_bool, direction, gears)


def score_count(gears):
    result = 0
    for i in range(4):
        if gears[i][0] == '1':
            result += (2**i)
    return result


cases=int(input())

for i in range(cases):
    number, direction = map(int, input().split())
    chain_reaction(number, direction)

solution = score_count(gears)

print(solution)


