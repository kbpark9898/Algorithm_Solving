#2019 kakao blind recruitment 1st test
#https://programmers.co.kr/learn/courses/30/lessons/42888

from collections import deque
# input_data= ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo",
# "Change uid4567 Ryan"]
# output_data=["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


def solution(record):
    user_data={}
    print_data=[]
    print_data=deque(print_data)
    answer = []
    for i in range(len(record)):
        current_string = record[i]
        current_string=current_string.split(' ')
        if current_string[0] == "Enter":
            user_data[current_string[1]]=current_string[2]
            print_data.append([current_string[1],'in'])
        elif current_string[0]=="Leave":
            print_data.append([current_string[1],'out'])
        else:
            user_data[current_string[1]]=current_string[2]
    
    for i in range(len(print_data)):
        current_data = print_data.popleft()
        if current_data[1] == 'in':
            answer.append(user_data[current_data[0]]+"님이 들어왔습니다.")
        else:
            answer.append(user_data[current_data[0]]+"님이 나갔습니다.")
    return answer

# print(solution(input_data))