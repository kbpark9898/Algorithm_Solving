sero, garo, rounds = map(int, input().split())
dominos =[]
is_damaged=[]
for i in range(sero):
    domino_line = list(map(int, input().split()))
    dominos.append(domino_line)
    is_damaged.append([1 for i in range(garo)])

answer=0
def attack(x_cord, y_cord, direction):
    global sero, garo, dominos, is_damaged, answer
    if is_damaged[x_cord][y_cord] == 1:
        is_damaged[x_cord][y_cord] = 0
        answer+=1
        if direction == 'E':
            length = dominos[x_cord][y_cord]
            for i in range(1,length):
                if y_cord+i<garo:
                    attack(x_cord, y_cord+i, 'E')   
        elif direction == 'W':
            length = dominos[x_cord][y_cord]
            for i in range(1,length):
                if y_cord-i>=0:
                    attack(x_cord, y_cord-i, 'W')       
        elif direction == 'S':
            length = dominos[x_cord][y_cord]
            for i in range(1,length):
                if x_cord+i<sero:
                    attack(x_cord+i, y_cord, 'S')    
        else:
            length = dominos[x_cord][y_cord]
            for i in range(1,length):
                if x_cord-i>=0:
                    attack(x_cord-i, y_cord, 'N')
                        

def defense(x, y):
    global dominos, is_damaged, garo, sero
    is_damaged[x][y]=1


def play(round):
    global answer, is_damaged, garo, sero
    for i in range(round):
        attack_x, attack_y, attack_dir = input().split()
        attack(int(attack_x)-1, int(attack_y)-1, attack_dir)
        defense_x, defense_y = map(int, input().split())
        defense(defense_x-1, defense_y-1)
    print(answer)
    for i in range(sero):
        for j in range(garo):
            if is_damaged[i][j] == 1:
                if j<garo-1:
                    print('S', end=' ')
                else:
                    print('S', end='')
            else:
                if j<garo-1:
                    print('F', end=' ')
                else:
                    print('F', end='')
        if i < sero-1:
            print()
    
play(rounds)