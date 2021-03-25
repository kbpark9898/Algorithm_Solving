from collections import deque
k=int(input())
testcase=[]
for i in range(k):
    a, b= map(int, input().split())
    testcase.append([a,b])

cal=['D', 'S', 'L', 'R']
def calculate(number, opt):
    result=number
    if opt =='D':
        result = result*2
        if result >9999:
            result = result%10000
    elif opt=='S':
        if number == 0:
            result = 9999
        else:
            result = number-1
    elif opt=='L':
        result = number%1000*10+number//1000
    else:
        result = number%10*1000 + number//10
    return result
    
def bfs(start, end, visited):
    global cal
    q = deque()
    q.append(start)
    while q:
        current_node = q.popleft()
        for i in range(4):
            next_node = calculate(current_node, cal[i])
            if visited[next_node]==0 and next_node != start:
                q.append(next_node)
                visited[next_node]=[cal[i], current_node]
                if next_node == end:
                    return

def tracking(visited, target):
    result=deque()
    previous = target
    while 1:
        before_node = visited[previous]
        if before_node ==0:
            answer = ''.join(result)
            return answer
        else:
            result.appendleft(before_node[0])
            previous=before_node[1]

for i in range(k):
    visited=[0 for i in range(10002)]
    current_testcase=testcase[i]
    if current_testcase[0] == current_testcase[1]:
        continue
    bfs(current_testcase[0], current_testcase[1], visited)
    answer = tracking(visited, current_testcase[1])
    print(answer)

        


