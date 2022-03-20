# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21

test = int(input())
result = []

for _ in range(test):
    dp = [1, 1, 1, 2, 2]
    n = int(input())

    if n <= 5:
        result.append(dp[n - 1]) 
    else:
        for i in range(5, n + 1):
            dp.append(dp[i - 1] + dp[i - 5]) 

        result.append(dp[n - 1])


for r in result:
    print(r)