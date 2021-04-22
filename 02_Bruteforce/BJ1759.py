from itertools import combinations

l, c = map(int, input().split())

string = list(input().split())

string.sort()

moum=['a', 'e', 'i', 'o', 'u']

def letter_check(word):
    global moum
    m_count=0
    j_count=0
    for i in word:
        if i in moum:
            m_count+=1
        else:
            j_count+=1
        if m_count>=1 and j_count>=2:
            return True
    if m_count>=1 and j_count>=2:
        return True
    else:
        return False

solution=[]
for comb in combinations(string, l):
    word = ''.join(list(comb))
    result = letter_check(word)
    if result:
        solution.append(word)

for i in solution:
    print(i)
