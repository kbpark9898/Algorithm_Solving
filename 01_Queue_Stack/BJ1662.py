compressed_s = input()
before_len = 0
stack=[]
for idx in range(len(compressed_s)):
    cur_char = compressed_s[idx]
    if cur_char != '(' and cur_char != ')':
        before_len+=1
    elif cur_char == '(':
        stack.append(before_len-1)
        stack.append(compressed_s[idx-1])
        before_len = 0
    else:
        cur_multiple = stack.pop()
        cur_add = stack.pop()
        before_len = int(cur_multiple)*before_len + int(cur_add)

print(before_len)