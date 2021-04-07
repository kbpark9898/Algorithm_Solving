k=int(input())
matrix = []

for i in range(k):
    matrix.append(list(map(int, input().split())))

visited=[[0 for i in range(k)]for i in range(k)]
visited[0][0] = 1
dx=[1, 0]
dy=[0, 1]

def check(matrix, start):
    global visited, dx, dy, k
    for i in range(k):
        for j in range(k):
            current_move = matrix[i][j]
            for delta in range(2):
                if current_move!=0:
                    X = i+dx[delta]*current_move
                    Y = j+dy[delta]*current_move
                    if X<k and Y<k:
                        visited[X][Y]+=visited[i][j]

check(matrix, [0,0])
print(visited[k-1][k-1])