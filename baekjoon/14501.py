n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(len(data)):
    t = data[i][0]
    p = data[i][1]
    try:
        if dp[i] < dp[i - 1]:
            dp[i] = dp[i - 1]
        dp[i + t] = max(dp[i] + p, dp[i + t])
    except:
        continue

print(max(dp))