sero, garo = map(int, input().split())
x, y, d = map(int, input().split())

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]


graph=[]
count=0
for i in range(sero):
    cur_list = list(map(int, input().split()))
    graph.append(cur_list)


def clean(graph):
    global garo, sero, dx, dy, count, x, y, d
    is_cleand = False
    dir_count = 1
    while dir_count<=4:
        if 0<=x<sero and 0<=y<garo:
            if graph[x][y] == 0:
                graph[x][y] = 2
                count+=1
            if d == 0:
                if y-1 >= 0:
                    if graph[x][y-1] == 0:
                        graph[x][y-1] = 2
                        d = 3
                        y-=1
                        is_cleand = True
                        count+=1
                        return 1
            elif d == 1:
                if x-1 >=0:
                    if graph[x-1][y] == 0:
                        graph[x-1][y] = 2
                        d = 0
                        x-=1
                        is_cleand = True
                        count+=1
                        return 1
            elif d == 2:
                if y+1 < garo:
                    if graph[x][y+1] == 0:
                        graph[x][y+1] = 2
                        d = 1
                        y+=1
                        is_cleand = True
                        count+=1
                        return 1
            elif d == 3:
                if x+1 < sero:
                    if graph[x+1][y] == 0:
                        graph[x+1][y] = 2
                        d = 2
                        x+=1
                        is_cleand = True
                        count+=1
                        return 1
            if not is_cleand:
                d+=3
                d = d%4
                dir_count+=1
          
    if not is_cleand:
        is_blocked = True
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 0<=X<sero and 0<=Y<garo and (graph[X][Y] ==0):
                is_blocked = False
        if is_blocked:
            if d == 0:
                if graph[x+1][y]==2:
                    x +=1
                    return 3
                else:
                    return 4
            elif d == 1:
                if graph[x][y-1] == 2:
                    y-=1
                    return 3
                else:
                    return 4
            elif d == 2:
                if graph[x-1][y] == 2:
                    x-=1
                    return 3
                else:
                    return 4
            elif d == 3:
                if graph[x][y+1] == 2:
                    y+=1
                    return 3
                else:
                    return 4
        else:
            return -1
            

    


def task(cur_cord, d, graph):
    global x, y
    return_value = -1
    while return_value != 4:
        return_value = clean(graph)

task([x, y], d, graph)
print(count)

    


    