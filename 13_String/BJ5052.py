testcase = int(input())
answer=[]
for i in range(testcase):
    cur_case = int(input())
    numbers=[]
    for i in range(cur_case):
        numbers.append(input())
    numbers.sort()
    is_break= False
    for i in range(1, cur_case):
        before_len = len(numbers[i-1])
        cur_len = len(numbers[i])
        if before_len<cur_len:
            if numbers[i-1] == (numbers[i])[0:before_len]:
                answer.append("NO")
                is_break = True
                break
    if not is_break:
        answer.append("YES")


for i in answer:
    print(i)