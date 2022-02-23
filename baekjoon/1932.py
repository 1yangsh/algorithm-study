n = int(input())
# dp[i][j] : i, j 도착했을 때 최댓값
# dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]
array = [[0] * (n + 1) for _ in range(n + 1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for j in range(1, i + 1):
        array[i][j] = tmp[j - 1]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]


print(max(dp[-1]))