# https://programmers.co.kr/learn/courses/30/lessons/67256
# 2020 카카오 인턴십 1번 - 키패드 누르기
# BFS 과정에서 있었던 실수를 찾아야한다!

# TC
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"  

from collections import deque

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

h={1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 
7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}

#bfs 과정에서 무슨 문제가 있을까..??
def bfs(start, target, dx, dy):
    visited=[[0,0,0]for i in range(4)]
    q=deque()
    q.append(start)
    visited[start[0]][start[1]]+=1
    while q:
        current_node = q.popleft()
        for i in range(4):
            X = current_node[0] + dx[i]
            Y = current_node[1] + dy[i]
            if [X,Y] == target:
                result = visited[current_node[0]][current_node[1]] + 1
                return result
            if 0<=X<4 and 0<=Y<3:
                if visited[X][Y] == 0:
                    q.append([X,Y])
                    visited[X][Y] = visited[current_node[0]][current_node[1]] + 1


#거리계산 이걸로하면 해결
def caclulate_distance(start, target):
    distance = abs(start[0] - target[0]) + abs(start[1] - target[1])
    return distance

current_left=h['*']
current_right=h['#']
left_numbers=[1, 4, 7]
right_numbers = [3, 6, 9]
result=[]
def play(numbers, hand):
    global current_left, current_right, left_numbers, right_numbers, result
    for i in numbers:
        if int(i) in left_numbers:
            result.append('L')
            current_left=h[i]
        elif int(i) in right_numbers:
            result.append('R')
            current_right=h[i]
        else:
            # if_left_distance= bfs(current_left, h[i], dx, dy)
            # if_right_distance = bfs(current_right, h[i], dx, dy)
            if_left_distance = caclulate_distance(current_left, h[i])
            if_right_distance = caclulate_distance(current_right, h[i])
            if if_left_distance > if_right_distance:
                result.append('R')
                current_right=h[i]
            elif if_left_distance < if_right_distance:
                result.append('L')
                current_left=h[i]
            else:
                if hand == "left":
                    result.append('L')
                    current_left=h[i]
                else:
                    result.append('R')
                    current_right=h[i]


def solution(numbers, hand):
    global result
    play(numbers, hand)
    answer = ''.join(result)
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

              


    
