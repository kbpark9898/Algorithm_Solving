import heapq

_list=[32, 16, 54, 94, 81, 31]

heapq.heapify(_list)
heapq.heappush(_list, 7)
print(heapq.heappop(_list))

print(heapq.heappushpop(_list, 100))

small_el=heapq.nsmallest(4, _list)
print(small_el)

big_el=heapq.nlargest(4, _list)
print(big_el)
print(len(_list))