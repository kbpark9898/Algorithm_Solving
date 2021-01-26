k=int(input())
number = 666
count=1
for i in range(667, 6670000):
    current_string = str(i)
    is_666 = current_string.find('666')
    print(is_666)
    if is_666!=-1:
        if number<i:
            number = i
            count+=1
    if count==k:
        break
print(number)
