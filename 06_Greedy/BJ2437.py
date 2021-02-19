k=int(input())
sinkers = list(map(int, input().split()))
sinkers = sorted(sinkers)

counter=0
for i in range(0, len(sinkers)):
    #counter+1에 유의
    if sinkers[i]>counter+1:
        break
    else:
        counter+=sinkers[i]

print(counter+1)