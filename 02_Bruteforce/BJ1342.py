#pypy3 메모리초과
#python3 통과
from itertools import permutations

def check(string):
    length = len(string)
    for i in range(1, length):
        if string[i] == string[i-1]:
            return False
    return True

result = 0

string = list(input())
h={}
for perm in permutations(string, len(string)):
    cur_string = ''.join(perm)
    if cur_string not in h and check(cur_string):
        result+=1
        h[cur_string] = 1
        

print(result)


