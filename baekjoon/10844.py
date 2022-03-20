n = int(input())

dp =[[0 for i in range(10)] for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = 1

dp[1][0] = 0


for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000

print(sum(dp[n]) % 1000000000)



    #   1 1 1 1 1 1 1 1 1
    #   2 2 2 2 2 2 2 2 1
    #   3 4 4 4 4 4 4 4 2