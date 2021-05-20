# 그리디 + 유니온파인드

g = int(input())
p = int(input())

parents = [i for i in range(g+1)]

gate_nums=[]

for i in range(p):
    gate_nums.append(int(input()))

def find(num):
    global parents
    if parents[num] == num:
        return num
    else:
        parents[num] = find(parents[num])
        return parents[num]

def union(first, second):
    global parents
    a = find(first)
    b = find(second)
    parents[b] = a


solution=0
for num in gate_nums:
    cur_parent = find(num)
    if cur_parent == 0:
        break
    else:
        solution+=1
        union(cur_parent-1, cur_parent)

print(solution)
