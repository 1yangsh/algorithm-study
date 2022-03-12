import sys
sys.setrecursionlimit(10**8)

def fibo(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 2] + dp[i - 1])

    return dp



test = int(input())
result = []
for _ in range(test):
    n = int(input())
    if n == 0:
        result.append((1, 0))
    else:
        dp = fibo(n)
        result.append([dp[-2], dp[-1]])


for a, b in result:
    print(a, b)

