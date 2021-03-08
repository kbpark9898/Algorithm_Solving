k=int(input())
liquid=list(map(int, input().split()))

liquid.sort()

left=0
right=0
answer_index=[]
#최대값 최소값 꼭 유의해서 확인하기.
result=3000000001

if_found=False
for i in range(k-2):
    if if_found==True:
        break
    if k==3:
        print(liquid[0], liquid[1], liquid[2])
        break
    left=i+1
    right=k-1
    while left<right:
        mix = liquid[i] + liquid[left] + liquid[right]
        if mix==0:
            answer_index=[i, left, right]
            if_found=True
            break
        elif abs(result)>=abs(mix):
            result = mix
            answer_index=[i, left, right]
        if mix<0:
            left+=1
        else:
            right-=1

print(liquid[answer_index[0]], liquid[answer_index[1]], liquid[answer_index[2]])
        
            
