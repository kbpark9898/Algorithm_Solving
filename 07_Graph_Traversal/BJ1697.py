from collections import deque
q=deque()

subin, sister = map(int, input().split())
result=0
visited=[0]*100001
def check(current, que, dst):
    global visited
    if current-1 >=0:
        if current-1 == dst:
            return 1
        if visited[current-1]==0:
            que.append(current-1)
            visited[current-1]=1
        
    if current+1 <=100000:
        if current+1 == dst:
            return 1
        if visited[current+1]==0:
            que.append(current+1)
            visited[current+1]=1
        
    if current*2 <= 100000:
        if current*2 == dst:
            return 1
        if visited[current*2]==0:
            que.append(current*2)
            visited[current*2]=1
    return 0

def bfs(start, end):
    global result
    global sister
    if start==end:
        return
    q.append(start)
    while q:
        result+=1
        length = len(q)
        for i in range(length):
            current_node = q.popleft()
            is_end=check(current_node, q, sister)
            if is_end:
                return

bfs(subin, sister)
print(result)
