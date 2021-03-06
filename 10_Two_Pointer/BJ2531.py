plate, menu_bound, continuity, coupon = map(int, input().split())
susi = []
for i in range(plate):
    susi.append(int(input()))
left = 0
right = continuity

susi = susi+ susi[:right-1]

def check(data, target):
    jiphap = set(data)
    if target in jiphap:
        return len(jiphap)
    else:
        return len(jiphap)+1

answer=0
while right<len(susi):
    answer = max(answer, check(susi[left:right], coupon))
    left+=1
    right+=1

print(answer)

    
    
    