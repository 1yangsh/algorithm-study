n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
data = list(zip(*data))

dp = [[0] * n for _ in range(m)]



for i in range(m):
    for j in range(n):
        if j != 0:
            dp[i][j] = data[i][j] + dp[i][j - 1]
        else:
            dp[i][j] = data[i][j] + dp[i - 1][-1]

k = int(input())

m = [list(map(int, input().split())) for _ in range(k)]
dp = sum(dp, [])
print(dp)


for i in m:
    if i[0] != 1 and i[1] != 1:
        m[((i[3] * m - 1) - 1) - (i[2] - n)] - m[((i[1] * m - 1) - 1) - (i[0] - n) - 1]

