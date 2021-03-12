# solution using union-find data structure

def find_parent(parent_list, node):
    if node != parent_list[node]:
        parent_list[node] = find_parent(parent_list, parent_list[node])
    return parent_list[node]



def union_p(parent_list, first_node, second_node):
    first_node = find_parent(parent_list, first_node)
    second_node = find_parent(parent_list, second_node)
    if first_node == second_node:
        return False
    parent_list[first_node] = second_node
    return True
        

result=[]
while 1:
    n, e= map(int, input().split())
    if n==0 and e==0: break
    parent=[i for i in range(n+1)]
    cycle =[0 for i in range(n+1)]
    for i in range(e):
        first_node, second_node = map(int, input().split())
        if not union_p(parent, first_node, second_node) : cycle[first_node]=1
    for i in range(1, n+1):
        cycle[find_parent(parent, i)] |= cycle[i]
    answer=0
    for i in range(1, n+1):
        if parent[i] == i and cycle[i] ==0:
            answer+=1
    result.append(answer)


case_count=1
if result:
    for answer in result:
        if answer>1:
            print("Case %d: A forest of %d trees." %(case_count, answer))
        elif answer==1:
            print("Case %d: There is one tree." %case_count)
        else:
            print("Case %d: No trees." %case_count)
        case_count+=1
