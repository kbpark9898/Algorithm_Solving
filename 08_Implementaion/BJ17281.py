from itertools import permutations
inning_count= int(input())
score = []
for i in range(inning_count):
    current_score = list(map(int, input().split()))
    score.append(current_score)

def baseball_play(perm_list):
    global score
    index=0
    got_score = 0
    for inning in score:
        out_count=0
        base=[0,0,0]
        while out_count<3:
            if inning[perm_list[index]]==0:
                out_count+=1
            elif inning[perm_list[index]]==1:
                got_score+=base[2]
                base[0], base[1], base[2] = 1, base[0], base[1]
            elif inning[perm_list[index]]==2:
                got_score+=base[2]+base[1]
                base[0], base[1], base[2] = 0, 1, base[0]
            elif inning[perm_list[index]]==3:
                got_score+=base[0]+base[1]+base[2]
                base[0], base[1], base[2] = 0, 0, 1
            elif inning[perm_list[index]]==4:
                got_score+=base[0]+base[1]+base[2] +1
                base[0], base[1], base[2] = 0, 0, 0
            index = (index+1)%9
    return got_score

solution=0
for perm in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):
    perm_list = list(perm)
    perm_list.insert(3, 0)
    solution = max(solution, baseball_play(perm_list))

        
        

print(solution)

