import sys
from itertools import combinations
from collections import deque

k = int(sys.stdin.readline())
result=[]
count = 0

def count_odd(number):
    current_odd = 0
    value = number
    while value//10 >0:
        if (value%10)%2 !=0:
            current_odd+=1
        value = value//10
    if (value%10)%2!=0:
        current_odd+=1
    return current_odd
   
def triple(number, a, b):
    first = int(number[:a])
    second = int(number[a:b])
    third = int(number[b:])
    return first+second+third
    
def double(number):
    return (number//10) + (number%10)

def split(k, count):
    global result
    str_value = str(k)
    str_len = len(str_value)
    count += count_odd(k)
    if str_len >=3:
        for comb in combinations(range(1, str_len), 2):
            value =triple(str_value, comb[0], comb[1])
            split(value, count)
    elif str_len == 2:
        value = double(k)
        split(value, count)
    else:
        result.append(count)


split(k, count)

print(min(result), max(result))