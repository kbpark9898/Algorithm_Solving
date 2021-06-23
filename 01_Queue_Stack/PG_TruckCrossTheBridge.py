#https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0 for i in range(bridge_length)]
    while q:
        answer+=1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                current_truck = truck_weights.pop(0)
                q.append(current_truck)
            else:
                q.append(0)

    return answer