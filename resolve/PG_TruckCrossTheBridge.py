#https://programmers.co.kr/learn/courses/30/lessons/42583

# resolve 0911
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_q = [0 for i in range(bridge_length)]
    while truck_weights:
        bridge_q.pop(0)
        if(sum(bridge_q) + truck_weights[0] <= weight):
            bridge_q.append(truck_weights.pop(0))
        else:
            bridge_q.append(0)
        answer+=1
    answer+=bridge_length
    return answer


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