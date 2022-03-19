n = int(input())

dp = [0] * (n + 1)


if n >= 3:
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
        

    print(dp[n])
else:
    dp = [1, 3, 5]
    print(dp[n - 1])