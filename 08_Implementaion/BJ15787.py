from collections import deque
import sys
k, commands=map(int, input().split())
train=[0 for i in range(k+1)]

#비트마스크 사용. 덱은 시간초과!

record=[]

def check_command(command, train_num, seat):
    global train
    if command == 1:
        train[train_num] |= (1<<seat)
    elif command == 2:
        train[train_num] = train[train_num]&~(1<<seat)
    elif command == 3:
        train[train_num] = train[train_num]<<1
        train[train_num] = train[train_num]&((1<<21)-1)

    else:
        train[train_num]=train[train_num]>>1
        train[train_num]=train[train_num]&~1

def result(train, record):
    for i in range(1, len(train)):
        current = train[i]
        if (current not in record):
            record.append(current)

def play(k, train):
    global commands, record
    for i in range(commands):
        command_set = list(map(int, sys.stdin.readline().split()))
        if len(command_set)==3:
            command = command_set[0]
            train_num = command_set[1]
            seat = command_set[2]
        else:
            command = command_set[0]
            train_num = command_set[1]
            seat = -1
        check_command(command, train_num, seat)
    result(train, record)

play(k, train)
answer = len(record)


print(answer)
        