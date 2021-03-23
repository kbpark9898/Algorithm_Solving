testcase = int(input())

#실패. bfs로 풀어야하나..???

def make_distatnce(current, target):
    x = abs(current[0] - target[0])
    y = abs(current[1] - target[1])
    return [x, y, x+y]


def check_visited(cord, visited_hash):
    key=str(cord[0])+str(cord[1])
    if key in visited_hash:
        return True
    else:
        return False


def check_nearlest(current, targetlist, visited_hash):
    distance=131072
    cord=[current[0], current[1]]
    for i in targetlist:
        if not check_visited(i, visited_hash):
            current_m_dis = make_distatnce(current, i)
            x=current_m_dis[0]
            y=current_m_dis[1]
            if distance > current_m_dis[2]:
                cord[0]=i[0]
                cord[1]=i[1]
                distance = current_m_dis[2]

    return cord


def validate_arrive(current, target):
    distance = make_distatnce(current, target)
    if distance[2] % 50 ==0:
        if distance[2] // 50 >20:
           return False
        else:
            return True
    else:
        if distance[2] // 50 >=20:
            return False
        else:
            return True


def all_cu_visited(hash, cu_list):
    if len(hash) == len(cu_list):
        return True
    else:
        return False

for turn in range(testcase):
    cu_count = int(input())
    visited_hash={}
    house=list(map(int,input().split()))
    cu_list=[]
    for i in range(cu_count):
        current_cu = list(map(int, input().split()))
        cu_list.append(current_cu)
    target=list(map(int, input().split()))
    is_happy=False
    current = house
    for i in range(cu_count):
        if validate_arrive(current, target):
            is_happy=True
            break
        else:
            next_cu = check_nearlest(current, cu_list, visited_hash)
            if next_cu != current:
                if validate_arrive(current, next_cu):
                    current = next_cu
                    visited_hash[str(current[0])+str(current[1])]=1
            else:
                break
    if validate_arrive(current, target):
        is_happy=True
    if is_happy:
        print("happy")
    else:
        print("sad")







    
