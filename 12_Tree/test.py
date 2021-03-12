test=[1, 2, 3, 4]

def plus(test):
    for i in range(len(test)):
        test[i] =test[i]+1

plus(test)
print(test)