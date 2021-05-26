# DFS + Tree + DP
import sys
if __name__ == "__main__":
    sys.setrecursionlimit(100000)

    employees, compliments = map(int, sys.stdin.readline().split())

    buha_jikwon=[[] for i in range(employees+1)]

    buha_input = list(map(int, sys.stdin.readline().split()))

    for i in range(1, len(buha_input)):
        buha_jikwon[buha_input[i]].append(i+1)

    dp=[0 for i in range(employees+1)]
    def dfs(start):
        global employees, buha_jikwon, dp
        emp_num, com_num = start
        for emp in buha_jikwon[emp_num]:
            dp[emp] += com_num
            dfs([emp, dp[emp]])

    #트리에 대한 dp정보를 한번에 갱신하고 dfs를 한번만 수행할것!
    #입력마다 dfs를 수행하면 시간초과
    for i in range(compliments):
        e_num, c_num=map(int, sys.stdin.readline().split())
        dp[e_num] += c_num
    dfs([1, dp[1]])
        

    for i in range(1, employees+1):
        print(dp[i], end=' ')
