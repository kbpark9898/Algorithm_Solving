#https://programmers.co.kr/learn/courses/30/lessons/43238

def condition(mid, times, n):
    result = 0
    for time in times:
        result+=mid//time
    if result >= n:
        return True
    else:
        return False

def p_search(left, right, times, n):
    while left<=right:
        mid = (left+right)//2
        check = condition(mid, times, n)
        if not check:
            left = mid + 1
        else:
            right = mid -1
    return left

def solution(n, times):
    left = 0
    right = n*(max(times))
    answer = p_search(left, right, times, n)
    return answer


