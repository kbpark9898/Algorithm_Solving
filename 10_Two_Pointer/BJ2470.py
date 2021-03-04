k=int(input())
liquid=list(map(int, input().split()))
liquid.sort()

left=0
right= len(liquid)-1
answer = 2000000001
current_liquid=[left, right]
while left<right:
    mix = liquid[left]+liquid[right]
    if mix==0:
        current_liquid[0]=left
        current_liquid[1]=right
        break
    if abs(answer) > abs(mix):
        current_liquid[0] = left
        current_liquid[1]=right
        answer = mix
    if mix<0:
        left+=1
    else:
        right-=1

print(liquid[current_liquid[0]], liquid[current_liquid[1]])