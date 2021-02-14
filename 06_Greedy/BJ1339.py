import heapq
k=int(input())
words=[]
for i in range(k):
    words.append(input())

words_dict={}

for word in words:
    word_len = len(word)-1
    for letter in word:
        if letter in words_dict:
            words_dict[letter]+=pow(10, word_len)
        else:
            words_dict[letter]=pow(10, word_len)
        word_len-=1

values=[]
heapq.heapify(values)
for value in words_dict.values():
    heapq.heappush(values, -value)

solution=0
number=9
for index in range(len(values)):
    solution+=(-heapq.heappop(values))*number
    number-=1

print(solution)