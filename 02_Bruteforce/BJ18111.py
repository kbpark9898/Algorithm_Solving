from collections import Counter
col, row, blocks = map(int, input().split())
array=[]
for i in range(col):
    data=list(map(int, input().split()))
    # array.append(data)
    array+=(data)
solution=[1000000000000000, 10000000000000000]
array_dict = dict(Counter(array))
_sum = sum(array)
solution_count=100000000000000000000
height = 0
for i in range(257):
    count=0
    if _sum+blocks>=i*col*row:
        for key in array_dict:
            if key>i:
                count+=(key-i)*2*array_dict[key]
            elif key<i:
                count+=(i-key)*array_dict[key]
        if solution_count>=count:
            height=i
            solution_count = count

print(solution_count, height)
            
            