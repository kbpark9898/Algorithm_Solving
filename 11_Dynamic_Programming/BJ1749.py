# DP + 구간합
import sys
if __name__ == '__main__':
    sero, garo = map(int, sys.stdin.readline().split())
    matrix = [[0 for i in range(garo+1)]]

    for i in range(sero):
        cur_list = [0] + list(map(int, sys.stdin.readline().split()))
        matrix.append(cur_list)
    result=200*200*(-100000)

    for i in range(1, sero+1):
        for j in range(1, garo+1):
            matrix[i][j] = matrix[i][j] + matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]


    for i in range(1, sero+1):
        for j in range(1, garo+1):
            for x in range(i, sero+1):
                for y in range(j, garo+1):
                    current_sum = matrix[x][y] - matrix[i-1][y] - matrix[x][j-1] + matrix[i-1][j-1]
                    result = max(result, current_sum)

    print(result)