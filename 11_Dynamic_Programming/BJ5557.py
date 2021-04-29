from collections import deque
import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
visited=[[0 for i in range(21)]for i in range(n-1)]

visited[0][numbers[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if visited[i-1][j] !=0 :
            next_number_plus = j + numbers[i]
            next_number_minus = j - numbers[i]
            if 0<=next_number_plus<=20:
                visited[i][next_number_plus] += visited[i-1][j]
            if 0<=next_number_minus<=20:
                visited[i][next_number_minus] += visited[i-1][j]

result = visited[n-2][numbers[-1]]
print(result)


        