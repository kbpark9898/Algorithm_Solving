#https://programmers.co.kr/learn/courses/30/lessons/43165

result=0
def dfs(index, cur_number, numbers, target):
    global result
    if index == len(numbers):
        if cur_number == target:
            result+=1
    else:
        dfs(index+1, cur_number+numbers[index], numbers, target)
        dfs(index+1, cur_number-numbers[index], numbers, target)
    return result

def solution(numbers, target):
    answer = dfs(0, 0, numbers, target)
    return answer
