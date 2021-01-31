#binary search code
def b_search(data, target):
    left = 0
    right = len(data)-1
    while left<=right:
        mid=(left+right)//2
        if target < data[mid]:
            right=mid-1
        elif target>data[mid]:
            left=mid+1
        else:
            return mid
    return -1
     

no_listen_num, no_saw_num = map(int, input().split())
no_listen=[]
no_saw=[]

solution=[]
for i in range(no_listen_num):
    no_listen.append(input())
for i in range(no_saw_num):
    no_saw.append(input())
no_listen.sort()
no_saw.sort()
for i in no_listen:
    if b_search(no_saw, i) != -1:
        solution.append(i)

print(len(solution))
solution.sort()
for i in solution:
    print(i)