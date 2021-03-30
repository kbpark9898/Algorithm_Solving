from copy import deepcopy
length = int(input())
dy=[-1, 0, 1]

def make_before_list(j, length, matrix):
    global dy
    before_list =[]
    for k in range(3):
        Y = j+dy[k]
        if 0<=Y<3:
            before_list.append(matrix[Y])
    return before_list

def max_memoization( matrix, dp):
    temp_dp=[0 for i in range(3)]
    for j in range(3):
        before_list = make_before_list(j, 3, dp)
        temp_dp[j] = matrix[j] + max(before_list)
    for j in range(3):
        dp[j] = temp_dp[j]

def min_memoization(matrix, dp):
    temp_dp=[0 for i in range(3)]
    for j in range(3):
        before_list = make_before_list( j, 3, dp)
        temp_dp[j] = matrix[j] + min(before_list)
    for j in range(3):
        dp[j]=temp_dp[j]
            

def make_result(flag, dp):
    result=0
    if flag==0:
        result = min(dp)
    else:
        result = max(dp)
    return result

def play( matrix, max_dp, min_dp):
    result=[]
    max_memoization(matrix, max_dp)
    result.append(make_result(1, max_dp))
    min_memoization(matrix, min_dp)
    result.append(make_result(0, min_dp))
    return result

matrix=[]
max_dp=list(map(int, input().split()))
min_dp = deepcopy(max_dp)
result=[]
if length==1:
    result.append(max(max_dp))
    result.append(min(min_dp))
for i in range(1, length):
    current_list = list(map(int, input().split()))
    result=play(current_list, max_dp, min_dp)
    

  
print(result[0], result[1])
