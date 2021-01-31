k=int(input())
data=set(map(int, input().split()))

input_size=int(input())
input_data=list(map(int,input().split()))

for i in input_data:
    if i in data:
        print(1)
    else:
        print(0)