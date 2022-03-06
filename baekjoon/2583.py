import sys
sys.setrecursionlimit(100000)


n, m, k = map(int, input().split())

data = [[0] * m  for _ in range(n)]


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            data[i][j] = 1


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    global cnt
    data[x][y] = 1
    cnt += 1

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if data[nx][ny] == 0:
            dfs(nx, ny)

    return cnt

result = []

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            cnt = 0
            result.append(dfs(i, j))


print(len(result))
for r in sorted(result):
    print(r, end=" ")



