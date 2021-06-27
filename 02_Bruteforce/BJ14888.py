from itertools import permutations
from copy import deepcopy
n = int(input())

numbers=list(map(int, input().split()))

opt = list(map(int, input().split()))

max_num = -1000000000
min_num = 1000000000

def devide(num1,num2):
    result = -1
    if num1 <0 :
        result = -(abs(num1) // num2)
    else:
        result = num1 // num2
    return result
opts=[]
for i in range(4):
    if i ==0:
        for j in range(opt[i]):
            opts.append('+')
    elif i ==1:
        for j in range(opt[i]):
            opts.append('-')
    elif i ==2:
        for j in range(opt[i]):
            opts.append('x')
    elif i ==3:
        for j in range(opt[i]):
            opts.append('/')

def brute_force(numbers, opt):
    global n, max_num, min_num, opts
    
    for perm in permutations(opts, n-1):
        copy_opt = deepcopy(opt)
        start_num = numbers[0]
        possible_max = True
        possible_min = True
        for i in range(1,n):
            if perm[i-1] =='+':
                start_num += numbers[i]
                copy_opt[0]-=1
            elif perm[i-1] =='-':
                start_num -= numbers[i]
                copy_opt[1]-=1
            elif perm[i-1] =='x':
                start_num *= numbers[i]
                copy_opt[2]-=1
            elif perm[i-1] =='/':
                start_num  = devide(start_num, numbers[i])
                copy_opt[3]-=1

            if start_num < max_num and copy_opt[0] == 0 and copy_opt[2] ==0:
                possible_max = False
            if start_num > min_num and copy_opt[1] == 0 and copy_opt[3] == 0:
                possible_min = False
            
            if possible_max == False and possible_min == False:
                break

        if max_num < start_num:
            max_num = start_num
        if min_num > start_num:
            min_num = start_num

brute_force(numbers, opt)
print(max_num)
print(min_num)



