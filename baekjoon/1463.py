n = int(input())


dp = [1, 0, 1, 1] + [0] * n

for i in range(4, n + 1):
    if i % 6 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1, dp[i - 1] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
    else:
        dp[i] = dp[i - 1] + 1


print(dp[n])