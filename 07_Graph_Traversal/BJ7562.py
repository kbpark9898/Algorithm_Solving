from collections import deque

testcase_count= int(input())
size=[]
current_node=[]
dst_node=[]
result=[]
for i in range(testcase_count):
    size.append(int(input()))
    current_node.append(list(map(int, input().split())))
    dst_node.append(list(map(int, input().split())))

d=[[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

def make_visited(size):
    visited=[]
    for i in range(size):
        _data=[]
        for j in range(size):
            _data.append(0)
        visited.append(_data)
    return visited
    
def bfs(current_size, x, y, dst_x, dst_y):
    global  d, result
    visited=make_visited(current_size)
    q=deque()
    q.append([x, y])
    visited[x][y]=1
    if x==dst_x and y==dst_y:
        result.append(0)
        return
    while q:
        length = len(q)
        for i in range(length):
            current_node = q.popleft()
            for j in range(8):
                X = current_node[0] + d[j][0]
                Y = current_node[1] + d[j][1]
                if X==dst_x and Y==dst_y:
                    result.append(visited[current_node[0]][current_node[1]])
                    return
                if X<0 or X>=current_size or Y<0 or Y>=current_size:
                    continue
                else:
                    if visited[X][Y] ==0:
                        visited[X][Y] = visited[current_node[0]][current_node[1]]+1
                        q.append([X,Y])
    result.append(visited[dst_x][dst_y])

for i in range(len(size)):
    bfs(size[i], current_node[i][0], current_node[i][1], dst_node[i][0], dst_node[i][1])


for i in range(len(result)):
    print(result[i])
    

