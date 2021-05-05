from itertools import permutations
import re
from copy import deepcopy
def solution(expression):
    operator_set = []
    for perm in permutations(['+', '-', '*'], 3):
        operator_set.append(perm)
    exp_split = re.split(r'(\D)', expression)

    results=[]
    for operators in operator_set:
        temp_exp = deepcopy(exp_split)
        for opt in operators:
            while opt in temp_exp:
                opt_index = temp_exp.index(opt)
                # print(type(temp_exp[opt_index-1]),type(temp_exp[opt_index]),type(temp_exp[opt_index+1]))
                current_calc_result = str(eval(temp_exp[opt_index-1]+temp_exp[opt_index]+temp_exp[opt_index+1]))
                temp_exp[opt_index-1] = current_calc_result
                temp_exp = temp_exp[:opt_index] + temp_exp[opt_index+2:]
        results.append(abs(int(temp_exp[0])))
    answer = max(results)
    return answer
