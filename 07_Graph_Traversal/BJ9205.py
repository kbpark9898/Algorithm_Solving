from collections import deque
testcase = int(input())


def check(src, dst):
    if abs(dst[0]-src[0]) + abs(dst[1] - src[1]) <=1000:
        return True
    else:
        return False

def bfs(start, target, stores):
    q = deque()
    q.append(start)
    visited_stores=[]
    while q:
        cur_node = q.popleft()
        if check(cur_node, target):
            return True
        index_list=[]
        for i in range(len(stores)):
            if stores[i] not in visited_stores and check(cur_node, stores[i]):
                q.append(stores[i])
                visited_stores.append(stores[i])
    return False

answer = []

for i in range(testcase):
    store_count = int(input())
    stores=[]
    start = list(map(int, input().split()))
    for i in range(store_count):
        stores.append(list(map(int, input().split())))
    target = list(map(int, input().split()))
    if bfs(start, target, stores):
        answer.append('happy')
    else:
        answer.append('sad')

for i in answer:
    print(i)
    

