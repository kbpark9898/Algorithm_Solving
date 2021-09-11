#https://programmers.co.kr/learn/courses/30/lessons/43164

# stack + DFS

# resolve 0911
routes={}

def make_routes(tickets):
    global routes
    for ticket in tickets:
        if(ticket[0] not in routes):
            routes[ticket[0]] = [ticket[1]]
        else:
            routes[ticket[0]].append(ticket[1])
    for key in routes:
        routes[key].sort()
        

def find_route(tickets, routes, answer):
    s = ['ICN']
    while len(s)>0:
        cur_place = s[len(s)-1]
        if((cur_place in routes) and len(routes[cur_place])>0):
            s.append(routes[cur_place].pop(0))
        else:
            print(s)
            answer.append(s.pop())

def solution(tickets):
    global routes
    answer = []
    make_routes(tickets)
    find_route(tickets, routes, answer)
    answer = answer[::-1]
    
    return answer
# routes={}
# def make_routes(tickets):
#     global routes
#     for ticket in tickets:
#         if ticket[0] not in routes:
#             routes[ticket[0]] = [ticket[1]]
#         else:
#             routes[ticket[0]].append(ticket[1])
#     for route in routes:
#         routes[route].sort()


# path=[]
# def dfs(tickets, routes):
#     global path
#     stack=["ICN"]
#     while stack:
#         cur_top = stack[-1]
#         if cur_top not in routes or len(routes[cur_top]) == 0:
#             path.append(stack.pop())
#         else:
#             stack.append(routes[cur_top].pop(0))

#     return path

    
    
# def solution(tickets):
#     global routes, path
#     make_routes(tickets)
#     answer = dfs(tickets, routes)
#     answer = answer[::-1]
#     return answer