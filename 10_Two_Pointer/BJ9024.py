testcase = int(input())

answer = []
for i in range(testcase):
    n, target = map(int, input().split())
    cur_list = list(map(int, input().split()))
    cur_list.sort()
    left = 0
    right = n-1
    cur_count = 0
    cur_diff = 300000000
    while left<right:
        cur_sum = cur_list[left] + cur_list[right]
        if abs(cur_sum - target)<= cur_diff:
                if abs(cur_sum-target) == cur_diff:
                    cur_count+=1
                else:
                    cur_count = 1
                    cur_diff = abs(cur_sum-target)
        if  cur_sum< target:
            left+=1
        else:
            right-=1
    answer.append(cur_count)

for i in answer:
    print(i)