import sys
#from collections import deque
photo_case_count = int(sys.stdin.readline())
rmd_count = int(sys.stdin.readline())

rmd = list(map(int, sys.stdin.readline().split()))

photo_case=[]

def find_student(photo_case, num):
	result=-1
	for i in range(len(photo_case)):
		if photo_case[i][0] == num:
			result = i
	return result

def find_min_student(photo_case):
	minimum = 1000
	result = -1
	for i in range(len(photo_case)):
		if photo_case[i][1] < minimum:
			minimum = photo_case[i][1]
			result = i
	return result

def recommend(num):
	global photo_case_count, photo_case
	result = find_student(photo_case, num)
	if len(photo_case)<photo_case_count:
		if result != -1:
			photo_case[result][1] +=1
		else:
			photo_case.append([num, 1])
	else:
		if result != -1:
			photo_case[result][1] +=1
		else:
			min_result = find_min_student(photo_case)
			photo_case.remove(photo_case[min_result])
			photo_case.append([num, 1])

def make_solution(photo_case):
	solution =[]
	for i in photo_case:
		solution.append(i[0])
	solution.sort()
	return solution

def play(rcmd):
	global photo_case
	for i in rcmd:
		recommend(i)
	solution = make_solution(photo_case)
	return solution

result=play(rmd)


for i in result:
	print(i, end=' ')
