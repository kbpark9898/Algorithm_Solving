#https://programmers.co.kr/learn/courses/30/lessons/43164

# stack + DFS
routes={}
def make_routes(tickets):
    global routes
    for ticket in tickets:
        if ticket[0] not in routes:
            routes[ticket[0]] = [ticket[1]]
        else:
            routes[ticket[0]].append(ticket[1])
    for route in routes:
        routes[route].sort()


path=[]
def dfs(tickets, routes):
    global path
    stack=["ICN"]
    while stack:
        cur_top = stack[-1]
        if cur_top not in routes or len(routes[cur_top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[cur_top].pop(0))

    return path

    
    
def solution(tickets):
    global routes, path
    make_routes(tickets)
    answer = dfs(tickets, routes)
    answer = answer[::-1]
    return answer