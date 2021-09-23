n, h = map(int ,input().split())
# n == 동굴의 길이
# h == 동굴의 높이

suksun = [0 for i in range(h+1)]
jongyousuck = [0 for i in range(h+1)]

for i in range(n):
    cur_height = int(input())
    if i%2==0:
        suksun[cur_height]+=1
    else:
        jongyousuck[cur_height]+=1


for i in range(h-1, 0, -1):
    suksun[i] += suksun[i+1]
    jongyousuck[i] += jongyousuck[i+1]


min_crush_count = n+1
section_count = 1

for i in range(1, h+1):
    if min_crush_count >= suksun[i] + jongyousuck[h-i+1]:
        if min_crush_count > suksun[i] + jongyousuck[h-i+1]:
            min_crush_count = suksun[i] + jongyousuck[h-i+1]
            section_count = 1
        else:
            section_count+=1

print(min_crush_count, section_count)



