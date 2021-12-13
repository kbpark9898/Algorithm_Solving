stack=[]
MAX = 2040001
x_cord = ['1' for i in range(MAX)]
n = int(input())
circles = []
for i in range(n):
    circles.append(list(map(int, input().split())))


def make_stack():
    global stack
    global MAX
    global x_cord
    global circles
    for circle in circles:
        if x_cord[circle[0]+(MAX//2)-circle[1]] != '1':
            return False
        x_cord[circle[0]+(MAX//2)-circle[1]] = [circle[0], '(']
        if x_cord[circle[0]+(MAX//2)+circle[1]] != '1':
            return False
        x_cord[circle[0]+(MAX//2)+circle[1]] = [circle[0], ')']
    

    for letter in x_cord:
        if letter != '1':
            if letter[1] == '(':
                stack.append(letter)
            elif letter[1] == ')':
                if stack[len(stack)-1][1] == '(' and stack[len(stack)-1][0] == letter[0]:
                    stack.pop()
                else:
                    return False
    return True

if make_stack():
    print('YES')
else:
    print('NO')