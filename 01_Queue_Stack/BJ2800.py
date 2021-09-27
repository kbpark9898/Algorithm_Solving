from itertools import combinations
from copy import deepcopy
formula = input()

stack=[]
brace_indexs=[]
for i in range(len(formula)):
    if formula[i] == '(':
        stack.append(i)
    elif formula[i] == ')':
        open_index = stack.pop()
        brace_indexs.append([open_index, i])

result = []
for i in range(1, len(brace_indexs)+1):
    for comb in combinations(brace_indexs, i):
        brace_cords=[]
        cur_string=''
        for cord in comb:
            brace_cords.append(cord[0])
            brace_cords.append(cord[1])
        for char_idx in range(len(formula)):
            if char_idx not in brace_cords:
                cur_string+=formula[char_idx]
        if cur_string not in result:
            result.append(cur_string)
            

result.sort()

for i in result:
    print(i)
        

