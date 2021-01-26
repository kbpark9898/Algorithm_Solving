input_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
for i in range(19):
    data=list(map(int, input().split()))
    data =[0]+data+[0]
    input_data.append(data)
input_data.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


#오른쪽으로 탐색
def right_search(data, color, x, y):
    count =1
    solution=[]
    found=False
    if 18-x>=5:
        for i in range(5):
            if data[x+i+1][y]==color:
                count+=1
            else:
                break
        if count ==5:
            found=True
    elif 18-x>=4:
        for i in range(4):
            if data[x+i+1][y]==color:
                count+=1
            else:
                break
        if count ==5:
            found=True
    return found


#오른쪽 아래로 탐색
def rightDown_search(data, color, x, y):
    count=1
    found=False
    if 18-x>=5 and 18-y>=5:
        for i in range(5):
            if data[x+i+1][y+i+1] == color:
                count+=1
            else:
                break
        if count==5:
            found=True
    elif 18-x>=4 and 18-y>=4:
        for i in range(5):
            if data[x+i+1][y+i+1] == color:
                count+=1
            else:
                break
        if count==5:
            found=True
    return found


#아래로 탐색
def down_search(data, color, x, y):
    count=1
    found=False
    if 18-y >=5:
        for i in range(5):
            if data[x][y+i+1]==color:
                count+=1
            else:
                break
        if count==5:
           found=True
    elif 18-y >=4:
        for i in range(5):
            if data[x][y+i+1]==color:
                count+=1
            else:
                break
        if count==5:
           found=True
            
    return found
    

#왼쪽 아래로 탐색
def leftDown_search(data, color, x, y):
    count=1
    found=False
    if x>=5 and 19-y>=5:
        for i in range(5):
            if data[x-i-1][y+i+1]==color:
                count+=1
            else:
                break
        if count==5:
            found=True
    elif x>=4 and 19-y>=4:
        for i in range(5):
            if data[x-i-1][y+i+1]==color:
                count+=1
            else:
                break
        if count==5:
            found=True

    return found

#위의 4개 함수를 사용하여 승리 여부를 판별
def omok():
    #승리조건 충족 여부를 판별하는 변수
    found=False

    #19*19의 리스트를 완전탐색
    for i in range(1, 20):
        if found:
            break
        for j in range(1, 20):
            if input_data[i][j]!=0:
                #각 판별함수를 적용하고, 판별함수를 적용하는 인덱스의 바로 전 인덱스에 해당하는 입력값을 확인하여 육목의 가능성 배제
                if right_search(input_data, input_data[i][j], i, j) and (input_data[i-1][j] != input_data[i][j]):
                    print(input_data[i][j])
                    print(i, j)
                    found=True
                    break
                elif rightDown_search(input_data, input_data[i][j], i, j)and(input_data[i-1][j-1]!=input_data[i][j]):
                    print(input_data[i][j])
                    print(i, j)
                    found=True
                    break
                elif down_search(input_data, input_data[i][j], i, j) and (input_data[i][j-1] != input_data[i][j]):
                    print(input_data[i][j])
                    print(i, j)
                    found=True
                    break            
                elif leftDown_search(input_data, input_data[i][j], i, j) and (input_data[i+1][j-1] != input_data[i][j]):
                    print(input_data[i-4][j+4])
                    print(i, j)
                    found=True
                    break
    #모든 인덱스에 대해 오목을 찾지 못했을 경우 0을 출력
    if found==False:
        print(0)

omok()