k=int(input())
data=[]
for i in range(k):
    data.append(int(input()))

data.sort()

for i in range(k):
    print(data[i])