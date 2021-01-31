import bisect

data=[1, 4, 5, 7, 9, 11,13, 13, 13, 15, 17, 19, 21, 25, 28, 31]
left=bisect.bisect_left(data, 13)
right=bisect.bisect_right(data, 13)
find=bisect.bisect(data, 13)
print(left, right, find)