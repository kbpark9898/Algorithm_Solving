from queue import PriorityQueue

test = PriorityQueue()
test.put((1, 'apple'))
test.put((1, 'grape'))
test.put((1, 'banana'))

for i in range(test.qsize()):
    print(test.get())