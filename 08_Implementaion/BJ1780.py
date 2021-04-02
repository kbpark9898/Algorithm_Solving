import sys
k=int(input())
matrix=[]
for i in range(k):
    current_list = list(map(int, sys.stdin.readline().split()))
    matrix.append(current_list)


def is_equal(matrix, length, start):
    first=matrix[start[0]][start[1]]
    for i in range(length):
        for j in range(length):
            if matrix[start[0]+i][start[1]+j] != first:
                return False
    return True

count={-1:0, 0:0, 1:0}
def devide_and_check(matrix, k, start):
    global count
    x=start[0]
    y=start[1]
    if is_equal(matrix, k, start):
        count[matrix[start[0]][start[1]]]+=1
    else:
        next_k=k//3
        devide_and_check(matrix, next_k, [x,y])
        devide_and_check(matrix, next_k, [x,y+next_k])
        devide_and_check(matrix, next_k, [x,y+next_k*2])
        devide_and_check(matrix, next_k, [x+next_k,y])
        devide_and_check(matrix, next_k, [x+next_k,y+next_k])
        devide_and_check(matrix, next_k, [x+next_k,y+next_k*2])
        devide_and_check(matrix, next_k, [x+next_k*2,y])
        devide_and_check(matrix, next_k, [x+next_k*2,y+next_k])
        devide_and_check(matrix, next_k, [x+next_k*2,y+next_k*2])

devide_and_check(matrix, k, [0,0])
print(count[-1])
print(count[0])
print(count[1])
        
    

