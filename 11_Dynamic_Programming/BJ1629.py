import sys
start, target, div = map(int, sys.stdin.readline().split())

def solution(start, target, div):
    if target ==1:
        return start % div
    elif target%2==0:
        result = solution(start, target//2, div)
        return result*result%div
    else:
        result=solution(start, (target-1)//2, div)
        return result*result*start%div

result = solution(start, target, div)
print(result)
        
