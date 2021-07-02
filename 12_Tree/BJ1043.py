# n = 사람 수, m = 파티 수

n, m = map(int, input().split())
known_people = list(map(int, input().split()))[1:]

party=[]
for i in range(m):
    cur_party = list(map(int, input().split()))[1:]
    cur_party.sort()
    party.append(cur_party)

parents=[i for i in range(n+1)]

def union(node1, node2):
    global parents
    r_node1 = find(node1)
    r_node2 = find(node2)
    parents[r_node2] = r_node1

def find(node):
    global parents
    if node != parents[node]:
        parents[node] = find(parents[node])
    return parents[node]

def make_tree(parents, party):
    for p in party:
        root = p[0]
        for i in range(1, len(p)):
            union(root, p[i])

def find_known_people(cur_party, parents):
    global known_people
    for person in cur_party:
        #union-find 외부에서 루트노드를 찾고자 할때도 항상 find함수를 이용하여 재귀적으로 찾아야함.
        cur_parent = find(person)
        for known in known_people:
            if cur_parent == find(known):
                return True
    return False
def solution(parents, party):
    global n, known_people
    make_tree(parents, party)
    result = 0
    for p in party:
        if not find_known_people(p, parents):
            result+=1
    return result

print(solution(parents, party))