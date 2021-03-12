# solution using union-find data structure
def find_parent(parent_list, node):
    if parent_list[node] != node:
        parent_list[node] = find_parent(parent_list, parent_list[node])
    return parent_list[node]
def union_p(parent_list, first_node, second_node):
    first_node = find_parent(parent_list, first_node)
    second_node = find_parent(parent_list, second_node)
    if first_node > second_node:
        parent_list[first_node] = second_node
    else:
        parent_list[second_node] = first_node
n=-1
e=-1
result=[]
while n!=0 and e!=0:
    
    n, e = map(int, input().split())
    if n==0 and e==0:
        break
    parent = [i for i in range(n+1)]
    counted_parent={}
    cycled_root={}
    answer=-1
    for i in range(len(parent)):
        counted_parent[i]=0
        cycled_root[i]=0
    for i in range(e):
        first_node, second_node = map(int, input().split())
        first_parent = find_parent(parent, first_node)
        second_parent = find_parent(parent, second_node)
        if first_parent == second_parent:
            cycled_root[first_parent] = 1
        else:
            #이미 사이클이 완성된 그래프에 새 노드를 추가하는 경우, 새롭게 결정될 부모노드 또한 사이클을 이룬 그래프의 부모 노드로 추가
            if cycled_root[first_node]==1 or cycled_root[second_node]==1:
                union_p(parent, first_node, second_node)
                cycled_root[parent[first_node]]=1
            union_p(parent, first_node, second_node)
    for i in parent:
        if cycled_root[i]==0:
            if counted_parent[i]==0:
                counted_parent[i]=1
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
