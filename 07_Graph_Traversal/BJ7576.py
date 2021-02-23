from collections import deque
import sys

garo, sero = map(int, input().split())
box=[]
for i in range(sero):
    data = list(map(int, input().split()))
    box.append(data)
q=deque()
for i in range(sero):
    for j in range(garo):
        if box[i][j] ==1:
            q.append([i, j])

result=-1
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def bfs():
    global result
    global q
    global dx
    global dy
    global box
    global garo
    global sero
    while q:
        result+=1
        length = len(q)
        for i in range(length):
            current_node = q.popleft()
            x=current_node[0]
            y=current_node[1]
            for j in range(4):
                X=x+dx[j]
                Y=y+dy[j]
                if X<0 or X>=sero or Y<0 or Y>=garo:
                    continue
                if box[X][Y]==0:
                    box[X][Y]=1
                    q.append([X, Y])

bfs()
for i in range(sero):
    for j in range(garo):
        if box[i][j] ==0:
            result = -1
            break
    if result==-1:
        break

print(result)



        