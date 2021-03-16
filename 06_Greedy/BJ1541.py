formula = input().split('-')

for i in range(len(formula)):
    current_formula = list(map(int, formula[i].split('+')))
    current_value = 0
    for item in current_formula:
        current_value+=item
    formula[i] = current_value



answer =int(formula[0])
for i in range(1, len(formula)):
    answer-=formula[i]


print(answer)