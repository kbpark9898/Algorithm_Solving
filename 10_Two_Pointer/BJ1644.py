n=int(input())
n +=1
sieve = [True] * n

# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:           # i가 소수인 경우
        for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
            sieve[j] = False

# 소수 목록 산출
prime_list = [i for i in range(2, n) if sieve[i] == True]
n-=1
answer=0
for i in range(1, len(prime_list)):
    prime_list[i] += prime_list[i-1]

#구간합을 구할때, 첫번째 원소부터 목표치까지 모든걸 더한 값이 n인 경우도 체크해주기 위한 조건문 (중요!)
if n in prime_list:
    answer+=1
left=0
right=0

while right<len(prime_list):
    section_sum = prime_list[right]-prime_list[left]
    if section_sum== n:
        answer+=1
    if section_sum<n:
        right+=1
    else:
        left+=1

print(answer)
        
