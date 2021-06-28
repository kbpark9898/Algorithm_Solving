
n = int(input())
numbers = list(map(int, input().split()))

target = [0 for i in range(n)]
count=0
def check_can_devide(target):
    global n
    for i in range(n):
        if target[i]%2 != 0:
            return False
    return True

def make_devide(numbers):
    global n, count
    for i in range(n):
        numbers[i] = numbers[i]//2
    count+=1

def make_minus_one(numbers):
    global n, count
    for i in range(n):
        if numbers[i] % 2 != 0:
            numbers[i]-=1
            count+=1

while numbers != target:
    check = check_can_devide(numbers)
    if check:
        make_devide(numbers)
    else:
        make_minus_one(numbers)


print(count)


