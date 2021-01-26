# from itertools import product

# test=[[1,3,4], [2,3], [1,4]]
# for i in product(test, repeat=3):
#     print(list(i))

# word=input()
# k=int(input())
# books=[]
# for i in range(k):
#     books.append(list(input().split()))
#     books[i][0] = int(books[i][0])

# word=list(word)
# word_in_books=[]
# for i in range(len(books)):
#     word_in_books.append([])

# for i in range(len(word)):
#     for j in range(len(books)):
#         if books[j][1].find(word[i])!=-1:
#             word_in_books[i].append(j)


# ANT
# 4
# 35000 COMPUTERARCHITECTURE
# 47000 ALGORITHM
# 43000 NETWORK
# 40000 OPERATINGSYSTEM

for i in range(1 <<5):
    print(i)



#     3 4 0
# 64 64 64 64
# 64 64 64 64
# 64 64 64 63