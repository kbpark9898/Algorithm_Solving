#sorting으로 분류했지만, hash 문제에 속해도 괜찮은 문제!
k=int(input())
number_list=list(map(int, input().split()))
number_hash={}
sorted_list =sorted(number_list)

count=0
for i in sorted_list:
    if i not in number_hash:
        number_hash[i]=count
        count+=1

for i in number_list:
    print(number_hash[i], end=' ')

#global config test