# https://programmers.co.kr/learn/courses/30/lessons/64062
# 2019 카카오 개발자 겨울 인턴십 / 징검다리 건너기
k=3
stones= [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

def is_triple_zero(input_data, mid, bound):
    zero_count=0
    for i in input_data:
        if(i<=mid):
            zero_count+=1
        else:
            zero_count=0
        if zero_count>=bound:
            return True
    return False

        

def p_search(data, bound):
    left=0
    right = 200000000
    while left<=right:
        mid=(left+right)//2
        if is_triple_zero(data, mid, bound):
            right=mid-1
        else:
            left=mid+1
    return left

print(p_search(stones, k))