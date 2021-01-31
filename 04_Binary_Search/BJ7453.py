import bisect
import sys
from itertools import product
#이분탐색 이용 풀이. BOJ 기준 시간초과로 통과 못함
#입력값 받기
k = int(input())
a=[]
b=[]
c=[]
d=[]

#product 함수 이용을 위한 인덱스 배열 형성
index=[i for i in range(k)]

#a, b, c, d 배열 제작
for i in range(k):
    q, w, e, r=map(int, sys.stdin.readline().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)

#이분탐색을 위한 a+b, -(c+d) 배열 
#2중 for문을 사용해 배열을 만들어도 똑같이 시간초과.
first_sum_data=[]
second_sum_data=[]
for prod in product(index, repeat=2):
    first_sum_data.append(a[prod[0]]+b[prod[1]])
    second_sum_data.append(-(c[prod[0]]+d[prod[1]]))

# a+b값을 -(c+d)배열에서 찾기위해 -(c+d) 배열을 정렬
second_sum_data.sort()
count=0

#이분탐색을 통해 (bisect) lower, upper 바운드를 계산. 
for i in first_sum_data:
    left=bisect.bisect_left(second_sum_data, i)
    #second_sum_data[left] 값이 i와 다르다면 i 값이 second_sum_data에 없다는 뜻이므로
    #upper bound를 계산하기 위한 이분탐색을 건너뜀
    if second_sum_data[left]!=i:
        continue
    right=bisect.bisect_right(second_sum_data, i)
    count+=(right-left)
print(count)


