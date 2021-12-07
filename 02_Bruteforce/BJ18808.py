map_sero, map_garo, sticker_count = map(int, input().split())

cur_map = [[0 for i in range(map_garo)] for j in range(map_sero)]

stickers=[]

for i in range(sticker_count):
    cur_sero, cur_garo = map(int, input().split())
    cur_s=[]
    for j in range(cur_sero):
        cur_s.append(list(map(int, input().split())))
    stickers.append(cur_s)

def turning_sticker(cur_s):
    cur_sero = len(cur_s)
    cur_garo = len(cur_s[0])
    devide = cur_sero//2
    # 0 1 2 3 4     abs(0-2) + devide = 4    0 1 2 3 abs(0-2) + 2 -1= 3, abs(1-2) +2 -1 = 2
    # 현재 행 개수가 홀수일경우 devide - cur_index + devide = 2devide - cur+index. 반복문은 devide까지 돌릴것.
    # 현재 행 개수가 짝수일 경우 2devide-cur_index-1. 반복문은 devide -1 까지 돌릴것.
    new_sticker = [[0 for i in range(cur_sero)] for j in range(cur_garo)]
    garo_sero_hash={}
    if cur_sero%2 ==0:
        for i in range(cur_sero):
            garo_sero_hash[i] = 2*devide-i-1
    else:
        for i in range(cur_sero):
            garo_sero_hash[i] = 2*devide-i
    
    for i in range(cur_sero):
        for j in range(cur_garo):
            new_cord=[j, garo_sero_hash[i]]
            new_sticker[j][garo_sero_hash[i]] = cur_s[i][j]
    return new_sticker

# 우선, 현재 스티커의 가로 혹은 세로가 노트북 격자의 가로 혹은 세로보다 더 큰지 확인
# 그 다음 스티커를 붙일 수 있는지 확인
# 못붙인다면 회전시켜서 붙일 수 있는지 확인
# 00 01 02 03 순으로 좌표 더해가며 격자의 가로 혹은 세로보다 더 큰지 확인하고 더 크다면 10부터 다시 확인
# 만약 열이 0인데 초과된다면 다음 스텝을 밟지 않기.
# 확인하는 과정은 현재 스티커가 1인 곳이 노트북 격자에서도 1이라면 좌표 옮겨서 다시 확인. 모든 좌표에 대해 불가하다면 스티커를 회전시켜서 처음부터 확인.

def isBiggerThanCurMap(s, add_garo, add_sero):
    global cur_map
    global map_garo
    global map_sero
    if(len(s[0])+add_garo <= map_garo and len(s)+add_sero <=map_sero):
        return False
    else: return True

def can_attach(s, add_garo, add_sero):
    global cur_map
    for sero in range(len(s)):
        for garo in range(len(s[0])):
            if cur_map[sero+add_sero][garo+add_garo] == 1 and s[sero][garo]==1:
                return False
    return True

def attach(s, add_garo, add_sero):
    global cur_map
    for sero in range(len(s)):
        for garo in range(len(s[0])):
            if s[sero][garo] == 1:
                cur_map[sero+add_sero][garo+add_garo] = s[sero][garo]

def check():
    global cur_map
    global stickers
    global map_garo
    global map_sero
    for sticker_index in range(len(stickers)):
        for direction in range(4):
            add_garo, add_sero = 0, 0
            is_attched = False
            while(add_sero<map_sero):
                if(not isBiggerThanCurMap(stickers[sticker_index], add_garo, add_sero)):
                    if(can_attach(stickers[sticker_index], add_garo, add_sero)):
                        attach(stickers[sticker_index], add_garo, add_sero)
                        is_attched = True
                        break
                    else:
                        add_garo+=1
                else:
                    add_sero+=1
                    add_garo=0
            if is_attched:
                break
            else:
                changed_sticker = turning_sticker(stickers[sticker_index])
                stickers[sticker_index] = changed_sticker

def count_empty():
    global cur_map
    global map_garo
    global map_sero
    result = 0
    for i in range(map_sero):
        for j in range(map_garo):
            if cur_map[i][j] == 1:
                result +=1
    return result

check()
print(count_empty())


            



