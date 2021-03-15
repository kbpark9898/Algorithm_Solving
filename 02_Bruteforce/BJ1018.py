sero, garo = map(int, input().split())
chessboard = []

for i in range(sero):
    chess_line = list(input())
    chessboard.append(chess_line)
    
def black_check(board, x, y):
    paint_count=0
    for i in range(8):
        for j in range(8):
            if i%2==0:
                if j%2==0:
                    if board[x+i][y+j] == 'W':
                        paint_count+=1
                else:
                    if board[x+i][y+j] == 'B':
                        paint_count+=1
            else:
                if j%2==0:
                    if board[x+i][y+j] == 'B':
                        paint_count+=1
                else:
                    if board[x+i][y+j] == 'W':
                        paint_count+=1
    return paint_count


def white_check(board, x, y):
    paint_count=0
    for i in range(8):
        for j in range(8):
            if i%2==0:
                if j%2==0:
                    if board[x+i][y+j] == 'B':
                        paint_count+=1
                else:
                    if board[x+i][y+j] == 'W':
                        paint_count+=1
            else:
                if j%2==0:
                    if board[x+i][y+j] == 'W':
                        paint_count+=1
                else:
                    if board[x+i][y+j] == 'B':
                        paint_count+=1
    return paint_count

def check(board, x, y):
    answer=100
    black = black_check(board, x, y)
    white = white_check(board, x, y)
    answer = min(black, white)
    return answer

result=1000
for i in range(sero):
    if i+7<sero:
        for j in range(garo):
            if j+7<garo:
                result = min(result, check(chessboard, i, j))

print(result)