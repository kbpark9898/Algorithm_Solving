from collections import deque

sero, garo = map(int, input().split())

graph = []
for i in range(sero):
	graph.append(list(input()))
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def find_start(graph, q):
	global garo, sero
	for i in range(sero):
		for j in range(garo):
			if graph[i][j] == 'S':
				q.append([i,j])
				return


def find_water(graph, q):
	global garo, sero
	for i in range(sero):
		for j in range(garo):
			if graph[i][j] == '*':
				q.append([i,j])

target=[]
def find_d(graph, target):
	global garo, sero
	for i in range(sero):
		for j in range(garo):
			if graph[i][j] == 'D':
				target.append(i)
				target.append(j)
count=0
def bfs():
	global garo, sero, graph, dx, dy, count
	ddj_q = deque()
	water_q = deque()
	find_start(graph, ddj_q)
	find_water(graph, water_q)
	water_len=len(water_q)
	ddj_len=1
	
	while ddj_q:
		next_water_len=0
		next_ddj_len=0
		if water_q:
			for i in range(water_len):
				current_water = water_q.popleft()
				for j in range(4):
					X = current_water[0] + dx[j]
					Y = current_water[1] + dy[j]
					if 0<=X<sero and 0<=Y<garo and (graph[X][Y]!='D' and graph[X][Y]!='X' and graph[X][Y]!='*'):
						graph[X][Y] = '*'
						water_q.append([X,Y])
						next_water_len+=1
		water_len=next_water_len
		count+=1
		for i in range(ddj_len):
			current_ddj = ddj_q.popleft()
			for i in range(4):
				X = current_ddj[0] + dx[i]
				Y = current_ddj[1] + dy[i]
				if (0<=X<sero) and (0<=Y<garo) and (graph[X][Y]=='.' or graph[X][Y]=='D'):
					if graph[X][Y] == 'D':
						graph[X][Y] = count
						return
					graph[X][Y] = count
					ddj_q.append([X,Y])
					next_ddj_len+=1				
		ddj_len = next_ddj_len 


find_d(graph, target)
bfs()
if graph[target[0]][target[1]] =='D':
	print("KAKTUS")
else:
	print(graph[target[0]][target[1]])

