# Programmers level 2
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer=list(number)
    stack=[answer[0]]
    count =k
    for i in answer[1:]:
        while len(stack)>0 and int(stack[-1])<int(i) and k>0:
            stack.pop()
            k-=1
        stack.append(i)
    if k!=0:
        stack=stack[:-k]
    answer = ''.join(stack)
    return answer

        

# num=input()
# k=int(input())
# print(solution(num, k))