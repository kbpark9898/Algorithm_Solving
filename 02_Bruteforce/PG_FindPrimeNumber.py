#https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
primenumbers={}
def solution(numbers):
    answer = string_permutation(list(numbers))
    return answer


def string_permutation(string_list):
    global primenumbers
    length = len(string_list)
    answer = 0
    for i in range(1, length+1):
        for perm in permutations(string_list, i):
            number = make_number(list(perm))
            if check_prime(number):
                if number not in primenumbers:
                    primenumbers[number] = 1
                    answer+=1
    return answer

def make_number(string_list):
    data = int(''.join(string_list))
    return data

def check_prime(number):
    if number == 1 or number ==0:
        return False
    for i in range(2, number):
        if number % i ==0:
            return False
    return True

# 댜른 풀이
# from itertools import permutations
# def prime_number(number):
#     for i in range(2, number):
#         if number%i==0:
#             return 0
#     return 1
# def solution(numbers):
#     string = list(numbers)
#     length=len(string)
#     string=[]
#     for i in range(length):
#         string += list(permutations(list(numbers), i+1))
#     prime_number_count=0
#     prime_number_list=[]
#     for i in range(len(string)):
#         number=int(''.join(string[i]))
#         if (number != 1) and(number!=0)and (prime_number(number)):
#             if number in prime_number_list:
#                 pass
#             else:
#                 prime_number_list.append(number)
#     return len(prime_number_list)