from collections import deque
subin, sister = map(int, input().split())

q=deque()
visited=[0]*100001
result=[-1]*100001

def check(start, end, que):
    global visited
    global result
    if start*2 <=100000:
        if visited[start*2] ==0:
            visited[start*2]=1
            que.appendleft(start*2)
            result[start*2]=result[start]
    if start+1 <=100000:
        if visited[start+1] ==0:
            visited[start+1]=1
            que.append(start+1)
            result[start+1]=result[start]+1
    if start-1 >=0:
        if visited[start-1] ==0:
            visited[start-1]=1
            que.append(start-1)
            result[start-1]=result[start]+1

def bfs():
    global q
    global subin
    global sister
    global visited
    global result
    q.append(subin)
    visited[subin]=1
    result[subin]=0
    equal=False
    if subin == sister:
        result[sister] = 0
        return
    while q:
        current_node = q.popleft()
        check(current_node, sister, q)


bfs()
print(result[sister])
        

