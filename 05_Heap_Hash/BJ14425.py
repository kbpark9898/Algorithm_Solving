import sys

n, m = map(int, sys.stdin.readline().split())

_dict={}
answer=0

for i in range(n):
    word=sys.stdin.readline()
    _dict[word]=1

for i in range(m):
    word=sys.stdin.readline()
    if word in _dict:
        answer+=1

print(answer)