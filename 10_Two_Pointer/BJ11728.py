first, second = map(int, input().split())

first_list = list(map(int ,input().split()))
second_list = list(map(int, input().split()))

solution=[]
first_pt=0
second_pt=0

while first_pt<first and second_pt<second:
    if first_list[first_pt]<second_list[second_pt]:
        solution.append(first_list[first_pt])
        first_pt+=1
    else:
        solution.append(second_list[second_pt])
        second_pt+=1

if first_pt>=first:
    for i in range(second_pt, second):
        solution.append(second_list[i])
else:
    for i in range(first_pt, first):
        solution.append(first_list[i])

for i in solution:
    print(i, end=' ')