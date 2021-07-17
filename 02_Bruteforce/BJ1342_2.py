#해쉬에 각 알파벳 개수를 저장하여, permutation의 카운트값을 각 알파벳 개수의 팩토리얼 값으로 나누면 중복 제거 가능
# abbbaa 에서, ababab에 대해 각 a 및 b를 index별로 다르게 취급한다면 중복이 생김
# 즉, 0번째 a : 1, 4번째 a : 2, 5번째 a : 3이라 한다면
# 1b2b3b / 1b3b2b / 2b1b3b... 가 모두 다름.
# 이때 나머지 문자를 고정한 상태에서 a의 위치들이 변경되는 경우의 수는 a의 개수를 팩토리얼 한것과 같다.
# 따라서 위와 같은 방법으로 중복 개수를 빼준다.
from itertools import permutations
import math

def check(string):
    length = len(string)
    for i in range(1, length):
        if string[i] == string[i-1]:
            return False
    return True

def make_hash(h, string):
    for i in string:
        if i in h:
            h[i]+=1
        else:
            h[i] = 1
result = 0

string = list(input())
h={}
make_hash(h, string)

for perm in permutations(string, len(string)):
    cur_string = ''.join(perm)
    if check(cur_string):
        result+=1
        
devide = 1
for i in h.values():
    devide*=math.factorial(i)

result = result // devide
print(result)


