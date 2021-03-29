# def condition_print(sero, garo, room):
#     for i in range(sero):
#         for j in range(garo):
#             print(room[i][j], end=' ')
#         print()
        
def spread(sero, garo, room):
    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    temp = [[0 for i in range(garo)] for i in range(sero)]
    for i in range(sero):
        for j in range(garo):
            if room[i][j] >0:
                spread_amount=0
                current_spread = room[i][j]//5
                for delta in range(4):
                    X=i+dx[delta]
                    Y=j+dy[delta]
                    if 0<=X<sero and 0<=Y<garo and room[X][Y]!=-1:
                        temp[X][Y]+=current_spread
                        spread_amount+= current_spread
                temp[i][j] +=room[i][j] - spread_amount
            elif room[i][j] ==-1:
                temp[i][j]=-1
    return temp


# 틀렸을때 clean_up 과 clean_down에서 인덱스 조절 명확하게 하지 않았음. 경계값 다시 확인하고 이해할것.

def clean_up(air_cord, sero, garo, room):
    # 공기청정기 윗부분 공기 순환
    upper_cord = air_cord[0]

    right_last = room[upper_cord[0]][garo-1]
    for i in range(garo-1, 1, -1):
        room[upper_cord[0]][i] = room[upper_cord[0]][i-1]
    room[upper_cord[0]][1] = 0

    #room[upper_cord[0]+1][garo-1]=right_last
    up_last=room[0][garo-1]
    for i in range(upper_cord[0]-1):
        room[i][garo-1]=room[i+1][garo-1]
    room[upper_cord[0]-1][garo-1]=right_last

    left_last=room[0][0]
    for i in range(garo-2):
        room[0][i] = room[0][i+1]
    room[0][garo-2]=up_last

    for i in range(upper_cord[0]-1, 1, -1):
        room[i][0] = room[i-1][0]
    room[1][0] = left_last


    

def clean_down(air_cord, sero, garo, room):
    # 공기청정기 아랫부분 공기 순환
    down_cord = air_cord[1]

    right_last = room[down_cord[0]][garo-1]
    for i in range(garo-1, 1, -1):
        room[down_cord[0]][i] = room[down_cord[0]][i-1]
    room[down_cord[0]][1] = 0

    
    down_last=room[sero-1][garo-1]
    for i in range(sero-1, down_cord[0]+1, -1):
        room[i][garo-1]=room[i-1][garo-1]
    room[down_cord[0]+1][garo-1] = right_last

    left_last=room[sero-1][0]
    for i in range(garo-2):
        room[sero-1][i] = room[sero-1][i+1]
    room[sero-1][garo-2]=down_last

    for i in range(down_cord[0]+1, sero-1):
        room[i][0] = room[i+1][0]
    room[sero-2][0]=left_last


def find_air_purifier(sero, room):
    for i in range(sero):
        if room[i][0] == -1:
            return [i,0], [i+1, 0]

def count_amount(sero, garo, room):
    result=0
    for i in range(sero):
        for j in range(garo):
            if room[i][j]>0:
                result+=room[i][j]
    return result

def play(sero, garo, time, room):
    upper_purifier, down_purifier = find_air_purifier(sero, room)
    puri_cord=[upper_purifier, down_purifier]
    for i in range(time):
        room = spread(sero, garo, room)
        clean_up(puri_cord, sero, garo, room)
        clean_down(puri_cord, sero, garo, room)
    result = count_amount(sero, garo, room)
    print(result)

sero, garo, time = map(int, input().split())
room=[]
for i in range(sero):
    current_list=list(map(int, input().split()))
    room.append(current_list)

play(sero, garo, time, room)


