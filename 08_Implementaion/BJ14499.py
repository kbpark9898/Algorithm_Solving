from copy import deepcopy

m, n, cur_cord_x, cur_cord_y, command_num= map(int, input().split())

cur_cord = [cur_cord_x, cur_cord_y]
graph = []
for i in range(m):
    current_garo = list(map(int, input().split()))
    graph.append(current_garo)

dice=[0,0,0,0,0,0]
commands = list(map(int, input().split()))
# 주사위 인덱스 매칭
#   0
# 4 1 5
#   2
#   3

def shift_dice(dice, command):
    copy_dice = deepcopy(dice)
    if command == 1:
        dice[4] = copy_dice[3]
        dice[1] = copy_dice[4]
        dice[5] = copy_dice[1]
        dice[3] = copy_dice[5]
    elif command == 2:
        dice[1] = copy_dice[5]
        dice[5] = copy_dice[3]
        dice[3] = copy_dice[4]
        dice[4] = copy_dice[1]
    elif command == 3:
        dice[0] = copy_dice[1]
        dice[1] = copy_dice[2]
        dice[2] = copy_dice[3]
        dice[3] = copy_dice[0]
    elif command == 4:
        dice[0] = copy_dice[3]
        dice[1] = copy_dice[0]
        dice[2] = copy_dice[1]
        dice[3] = copy_dice[2]
    return dice

dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]

def move_dice(dice, graph, cur_cord, command):
    global m, n, dx, dy
    cur_cord[0]+=dx[command-1]
    cur_cord[1]+=dy[command-1]
    if 0<=cur_cord[0]<m and 0<=cur_cord[1]<n:
        shift_dice(dice, command)
        if graph[cur_cord[0]][cur_cord[1]] == 0:
            graph[cur_cord[0]][cur_cord[1]] = dice[3]
        else:
            dice[3] = graph[cur_cord[0]][cur_cord[1]]
            graph[cur_cord[0]][cur_cord[1]] = 0
        print(dice[1])
    else:
        cur_cord[0]-=dx[command-1]
        cur_cord[1]-=dy[command-1]
        

def play(command_num):
    global dice, graph, cur_cord, commands
    for i in range(command_num):
        move_dice(dice, graph, cur_cord, commands[i])


play(command_num)


    