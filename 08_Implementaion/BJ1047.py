#시간초과! 해결방법은..??
# 전체 사각형을 분할하며 모두 탐색하지않고, 각 분할된 사각형의 첫번째 칸 값을 하드하게 계산하자.
# 이렇게 사각형을 분할해가며 target 좌표가 포함된 최소범위의 사각형 까지 쪼개고, 최소범위 사각형에서 z 형태 재귀탐색!
import sys
n, target_x, target_y = map(int, sys.stdin.readline().split())
dx=[0, 1, 1]
dy=[1, 0, 1]
before_count = -1
def dfs(n, start):
    global dx, dy, before_count
    if n>2:
        cur_n = int(n//2)
        dfs(cur_n, start)
        dfs(cur_n,[start[0], start[1]+cur_n])
        dfs(cur_n, [start[0]+cur_n, start[1]])
        dfs(cur_n, [start[0]+cur_n, start[1]+cur_n])
    else:
        before_count+=1
        for i in range(3):
            X=start[0] + dx[i]
            Y=start[1] + dy[i]
            before_count+=1
            if X==target_x and Y==target_y:
                print(before_count)
                return      
dfs(pow(2, n), [0,0])
