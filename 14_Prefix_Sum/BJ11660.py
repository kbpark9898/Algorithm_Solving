n, m = map(int, input().split())

prefix=[]

for i in range(n):
    cur_list = list(map(int, input().split()))
    prefix.append(cur_list)

prefix_sum=[[0 for i in range(n)] for i in range(n)]

prefix_sum[0][0] = prefix[0][0]

for i in range(1, n):
    prefix_sum[0][i] = prefix_sum[0][i-1] + prefix[0][i]
    prefix_sum[i][0] = prefix_sum[i-1][0] + prefix[i][0]

for i in range(1, n):
    for j in range(1, n):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + prefix[i][j] -prefix_sum[i-1][j-1]


answer = []
for count in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    src = [x1-1, y1-1]
    dst = [x2-1, y2-1]
    sub_sum1_cord = [dst[0], src[1]-1]
    sub_sum2_cord = [src[0]-1, dst[1]]
    add_sum_cord = [src[0]-1, src[1]-1]
    result = prefix_sum[dst[0]][dst[1]]
    is_sub_sum1 = False
    is_sub_sum2 = False
    if sub_sum1_cord[0]>=0 and sub_sum1_cord[1]>=0:
        result-=prefix_sum[sub_sum1_cord[0]][sub_sum1_cord[1]]
        is_sub_sum1= True
    if sub_sum2_cord[0] >=0 and sub_sum2_cord[1] >=0:
        result-=prefix_sum[sub_sum2_cord[0]][sub_sum2_cord[1]]
        is_sub_sum2 = True
    if is_sub_sum1== True and is_sub_sum2 == True:
        result+=prefix_sum[add_sum_cord[0]][add_sum_cord[1]]
    answer.append(result)
    

for ans in answer:
    print(ans)
