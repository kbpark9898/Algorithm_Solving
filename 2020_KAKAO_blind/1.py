def slice_string(s, n):
    entire_string = s
    splited=[]
    while len(entire_string)>=n:
        splited.append(entire_string[:n]) 
        entire_string = entire_string[n:]
    if len(entire_string)>0:
        splited.append(entire_string)
    return splited
def make_counted_string(splited):
    counted_string=''
    cur_index = 0
    while cur_index < len(splited):
        count = 0
        for i in range(cur_index+1, len(splited)):
            if splited[cur_index] == splited[i]:
                count+=1
            else:
                break
        counted_string+= f'{count+1}{splited[cur_index]}' if count>=1 else f'{splited[cur_index]}'
        cur_index+=count+1
    return counted_string

def play(s, max_len):
    result = 10000
    for i in range(1, max_len+1):
        cur_res = make_counted_string(slice_string(s, i))
        result = min(result, len(cur_res))
    return result
        
def solution(s):
    length = len(s)
    if length == 1:
        return 1
    answer = play(s, len(s)//2)
    return answer