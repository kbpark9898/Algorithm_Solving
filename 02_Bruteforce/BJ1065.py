k=input()
slice_input=list(k)
k=int(k)
for i in range(len(slice_input)):
    slice_input[i] = int(slice_input[i])

def make_slice(number):
    data = list(str(number))
    for i in range(len(data)):
        data[i]=int(data[i])
    return data


if len(slice_input)<=2:
    print(k)
else:
    count=99
    for num in range(100, k+1):
        is_hansu=True
        current_number = make_slice(num)
        first_inc=current_number[1]-current_number[0]
        for i in range(2, len(current_number)):
            if (current_number[i]-current_number[i-1])!=first_inc:
                is_hansu=False
                break
        if is_hansu:
            count+=1
    print(count)