# memoization + BFS

from collections import deque
from copy import deepcopy
n = int(input())

# 초기노드 = [화면의 이모티콘 수, 클립보드에 있는 이모티콘 수, 걸린 시간]
start=[1, 0, 0]

# memo 위한 dp 배열
dp=[[0 for i in range(2000)] for i in range(2000)]
def bfs(start):
    global dp, n
    q = deque()
    q.append(start)
    dp[start[2]][start[0]] = 1
    while q:
        cur_node = q.popleft()
        if cur_node[0] == n:
            return cur_node[2]
        copy_node = [cur_node[0], cur_node[0], cur_node[2]+1]
        if cur_node[1] != copy_node[1]:
            q.append(copy_node)
        if cur_node[0]>2 and dp[cur_node[1]][cur_node[0]-1] ==0:
            copy_node = deepcopy(cur_node)
            copy_node[0]-=1
            copy_node[2]+=1
            q.append(copy_node)
            dp[copy_node[1]][copy_node[0]] = copy_node[2]
        if cur_node[0] < 2000 and cur_node[1]< 2000 and cur_node[0]+cur_node[1] < 2000:
            if dp[cur_node[1]][cur_node[0]+cur_node[1]] == 0 and cur_node[1]>0 :
                copy_node = deepcopy(cur_node)
                copy_node[0] += copy_node[1]
                copy_node[2] += 1
                q.append(copy_node)
                dp[copy_node[1]][copy_node[0]] = copy_node[2]
    return
result = bfs(start)
print(result)

         