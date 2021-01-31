k=int(input())
data=[]
for i in range(k):
    age, name = input().split()
    age=int(age)
    data.append((age, name))

data = sorted(data, key=lambda data :data[0])

for i in range(k):
    print(data[i][0], data[i][1])