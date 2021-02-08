import sys
k=int(input())
line=dict(zip(list(map(int, sys.stdin.readline().split())), [1 for i in range(k)]))
find_k=int(input())
find_line=list(map(int,sys.stdin.readline().split()))

for i in find_line:
    if i in line:
        print(1)
    else:
        print(0)
