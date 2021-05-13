n, m, k= map(int, input().split())

graph = [[[]for i in range(n+1)]for i in range(n+1)]

for i in range(m):
    current_fireball = list(map(int, input().split()))
    graph[current_fireball[0]][current_fireball[1]].append(current_fireball[2:])

#파이어볼 = [질량, 속도, 방향]
#합쳐지는 파이어볼들의 방향이 모두 짝수이거나 홀수이면 각각 0, 2, 4, 6으로 쪼개짐
#그게 아니라면 각각 1, 3, 5, 7로 쪼개짐
direction_h={0:[-1, 0], 1:[-1, 1], 2:[0, 1], 3:[1, 1], 4:[1, 0], 5:[1, -1], 6:[0, -1], 7:[-1, -1]}
def move_fireball():
    global graph, n, direction_h
    temp_graph = [[[]for i in range(n+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            for fireball in graph[i][j]:
                move = direction_h[fireball[2]]
                delta_x = (move[0]*fireball[1])%n
                move_x = i+delta_x
                move_x = (move_x+n)%n+1
                delta_y = (move[1]*fireball[1])%n
                move_y = j+delta_y
                move_y = (move_y+n)%n+1
                temp_graph[move_x][move_y].append(fireball)
    graph=temp_graph

def define_m(fireball_list):
    m_sum=0
    for i in fireball_list:
        m_sum+=i[0]
    return m_sum//5

def define_s(fireball_list):
    s_sum = 0
    for i in fireball_list:
        s_sum+=i[1]
    return s_sum//len(fireball_list)

def define_d(fireball_list):
    jjak, hol = 0, 0
    for i in fireball_list:
        if i[2]%2==0:
            jjak+=1
        else:
            hol+=1
    if jjak==0 or hol ==0:
        return [0, 2, 4, 6]
    else:
        return [1, 3, 5, 7]

def devide_fireball(fireball_list, cur_cord):
    global graph
    current_m = define_m(fireball_list)
    current_s = define_s(fireball_list)
    current_d = define_d(fireball_list)
    graph[cur_cord[0]][cur_cord[1]]=[]
    if current_m>0:
        for i in range(4):
            current_fireball = [current_m, current_s, current_d[i]]
            graph[cur_cord[0]][cur_cord[1]].append(current_fireball)


def sum_m(graph):
    global n
    solution = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for item in graph[i][j]:
                solution+=item[0]
    return solution

def play():
    global n, m, k , graph
    for i in range(k):
        move_fireball()
        for x in range(1, n+1):
            for y in range(1, n+1):
                if len(graph[x][y])>1:
                    devide_fireball(graph[x][y], [x, y])
    print(sum_m(graph))

play()

