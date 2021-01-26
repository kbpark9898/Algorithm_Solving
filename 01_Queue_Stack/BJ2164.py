from collections import deque
n=input()
cardSet = deque([i for i in range(1, int(n)+1)])

while len(cardSet)>=2:
    cardSet.popleft()
    data = cardSet.popleft()
    cardSet.append(data)
print(cardSet.pop())
