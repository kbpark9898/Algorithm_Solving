import sys
testcase = int(sys.stdin.readline())
answer=[]
for case in range(testcase):
    n, m, k = map(int, sys.stdin.readline().split())
    house = list(map(int, sys.stdin.readline().split()))
    result=0
    right=0
    length=0
    current_sum=0
    if n!=m:
        for left in range(n):
            while right<n+m-1 and length<m:
                length+=1
                current_sum+=house[right%n]
                right+=1
            if current_sum<k:
                result+=1
            length-=1
            current_sum-=house[left]
        answer.append(result)
    else:
        if sum(house)<k:
            answer.append(1)
        else:
            answer.append(0)
    # 시간초과
    # if n != m:
    #     while left<len(house):
    #         if right <len(house):
    #             current_sum = sum(house[left:right+1])
    #             if current_sum<k:
    #                 result+=1
    #         else:
    #             modulo_right = right%len(house)
    #             current_sum = sum(house[left:])+sum(house[:modulo_right+1])
    #             if current_sum<k:
    #                 result+=1
    #         left+=1
    #         right+=1
    #     answer.append(result)
    # else:
    #     if sum(house) < k:
    #         answer.append(1)
for i in answer:
    print(i)


