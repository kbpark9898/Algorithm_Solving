import copy

sero, garo = map(int, input().split())
graph=[]
for i in range(sero):
    cur_list = list(input().split())
    graph.append(cur_list)
cctv_list=[]
cctv_num=0
cctv_hash={
    '1' : [[0], [1], [2], [3]],
    '2' : [[0, 2], [1, 3]],
    '3' : [[0, 1], [1, 2], [2, 3], [3, 0]],
    '4' : [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    '5' : [[0, 1, 2, 3]]
}

direction_hash={
    0 : [-1, 0],
    1 : [0, 1],
    2 : [1, 0],
    3 : [0, -1]
}

def find_route_recursive(start_cord, dirnum, cur_graph):
        d_cord = direction_hash[dirnum]
        dx = start_cord[0] + d_cord[0]
        dy = start_cord[1] + d_cord[1]
        if(0<=dx<sero and 0<=dy<garo and cur_graph[dx][dy]!='6'):
            cur_graph[dx][dy] = '#'
            find_route_recursive([dx, dy], dirnum, cur_graph)
        else:
            return

def find_route(start_cord, direction, cur_graph):
    global sero, garo
    for dirnum in direction:
        find_route_recursive(start_cord, dirnum, cur_graph)
        

def count_route(cur_graph):
    cur_count = 0
    for i in range(sero):
        for j in range(garo):
            if(cur_graph[i][j] == '0'):
                cur_count+=1
    return cur_count

def count_cctv(graph):
    global garo, sero, cctv_list, cctv_num
    for i in range(sero):
        for j in range(garo):
            if(1<=int(graph[i][j])<=5):
                cctv_num+=1
                cctv_list.append([i, j, graph[i][j]])

count_cctv(graph)

answer = 99999999
def dfs(cur_num, cur_graph):
    global garo, sero, cctv_list, cctv_num, cctv_hash, answer
    if cctv_num == cur_num:
        cur_count = count_route(cur_graph)
        answer = min(answer, cur_count)
        return
    cur_cctv = cctv_list[cur_num]
    cur_cctv_direction = cctv_hash[cur_cctv[2]]
    for i in range(len(cur_cctv_direction)):
        new_graph = copy.deepcopy(cur_graph)
        find_route(cur_cctv, cur_cctv_direction[i], new_graph)
        new_num = cur_num+1
        dfs(new_num, new_graph)
    return

dfs(0, graph)

print(answer)



