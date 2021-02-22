from collections import deque
import sys

def find_level(_data):
    current = abs(_data[0] - _data[1])
    for i in range(1, len(_data)-1):
        next_sub = abs(_data[i]-_data[i+1])
        if current < next_sub:
            current = next_sub
    if current < abs(_data[0] - _data[len(_data)-1]):
        current= abs(_data[0] - _data[len(_data)-1])
    return current


k = int(input())
result=[]
for i in range(k):
    wood=[]
    wood = deque(wood)
    count = int(input())
    wood_data = list(map(int, sys.stdin.readline().split()))
    wood_data.sort(reverse=True)
    for index in range(len(wood_data)):
        if index%2==0:
            wood.appendleft(wood_data[index])
        else:
            wood.append(wood_data[index])
    result.append(find_level(wood))

for i in range(len(result)):
    print(result[i])

