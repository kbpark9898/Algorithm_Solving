n, k= input().split()
n = int(n)
k = int(k)-1
index = k
data = [i for i in range(1, n+1)]
solution=[]
while len(data)>=2:
    if index>len(data)-1:
        index=index%len(data)
        pop_data = data.pop(index)
        solution.append(str(pop_data))
    else:
        pop_data = data.pop(index)
        solution.append(str(pop_data))
    index+=k
solution.append(str(data.pop()))
solution_string = '<'+', '.join(solution)+'>'
print(solution_string)

