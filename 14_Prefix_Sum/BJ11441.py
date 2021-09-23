items = int(input())

data = list(map(int, input().split()))

prefix_sum = [data[0]]
for i in range(1, items):
    prefix_sum.append(prefix_sum[i-1] + data[i])


sum_count = int(input())

answer = []
for i in range(sum_count):
    result = 0
    src, dst = map(int, input().split())
    src-=1
    dst-=1
    if src == 0:
        result = prefix_sum[dst]
    else:
        result = prefix_sum[dst] - prefix_sum[src-1]
    answer.append(result)

for i in answer:
    print(i)