from itertools import product
sero, garo = map(int, input().split())
matrix=[]
for i in range(sero):
    current_list = list(input())
    matrix.append(current_list)

bitmap=[]

for prod in product([0,1], repeat=sero*garo):
    prod_list = list(prod)
    current_bitmap=[]
    for i in range(sero):
        current_bitmap.append(prod_list[i*garo:(i+1)*garo])
    bitmap.append(current_bitmap)

result = -1
for bmap in bitmap:
    formula=[]
    for i in range(sero):
        for j in range(garo):
            current_number=''
            if bmap[i][j] == 1:
                current_number+=matrix[i][j]
                bmap[i][j]=2
                cur_j = j+1
                while cur_j < garo and bmap[i][cur_j]==1:
                    current_number+=matrix[i][cur_j]
                    bmap[i][cur_j]=2
                    cur_j+=1
            elif bmap[i][j] == 0:
                current_number+=matrix[i][j]
                bmap[i][j]=2
                cur_i = i+1
                while cur_i < sero and bmap[cur_i][j] == 0:
                    current_number+=matrix[cur_i][j]
                    bmap[cur_i][j]=2
                    cur_i+=1
            if current_number != '':
                formula.append(int(current_number))
    result = max(result, sum(formula))

print(result)


