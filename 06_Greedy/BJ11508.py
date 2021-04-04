n=int(input())
price=[]
for i in range(n):
    price.append(int(input()))
price.sort(reverse = True)

result=0

for i in range(n):
    if i%3 != 2:
        result+=price[i]

print(result)