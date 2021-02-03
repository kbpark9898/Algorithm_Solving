# import bisect

# data=[1, 4, 5, 7, 9, 11,13, 13, 13, 15, 17, 19, 21, 25, 28, 31]
# left=bisect.bisect_left(data, 13)
# right=bisect.bisect_right(data, 13)
# find=bisect.bisect(data, 13)
# print(left, right, find)

stones= [2, 4, 0, 0, 1, 1, 0, 2, 5, 1]
stones=map(str, stones)
join_data=''.join(stones)
if join_data.find('000')!=-1:
    print('yes')
else:
    print("no")

print(join_data)