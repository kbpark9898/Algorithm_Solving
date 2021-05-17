from collections import deque

testcases = int(input())
solution=[]
for i in range(testcases):
    command = input()
    length = int(input())
    string = input()
    if string=='[]':
        string=[]
    else:
        string = list(string[1:-1].split(','))
    string = deque(string)
    is_reversed = 0
    is_broken = False
    for letter in command:
        if letter == 'R':
            is_reversed += 1
        else:
            if string:
                if is_reversed % 2 == 0:
                    string.popleft()
                else:
                    string.pop()
            else:
                solution.append('error')
                is_broken = True
                break
    if not is_broken:
        result=[]
        if is_reversed%2==0:
            for char in string:
                result.append(char)

            solution.append('['+(','.join(result))+']')
        else:
            for index in range(len(string)-1, -1, -1):
                result.append(string[index])
            solution.append('['+(','.join(result))+']')


for i in solution:
    print(i)
    

