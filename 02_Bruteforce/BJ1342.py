from itertools import permutations

def check(string):
    length = len(string)
    for i in range(1, length):
        if string[i] == string[i-1]:
            return False
    return True

result = 0

string = list(input())
h=[]


for perm in permutations(range(len(string)), len(string)):
    cur_string = ''
    for i in perm:
        cur_string+=string[i]
    if cur_string not in h and check(cur_string):
        result+=1
        h.append(cur_string)

        
print(result)


