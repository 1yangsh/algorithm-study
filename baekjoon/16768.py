n, k = map(int, input().split())

m = [list(input()) for _ in range(n)]
visited = [[0] * 10 for _ in range(n)]

def dfs(num, x, y, cnt):
    visited[x][y] = 1
    dx = (0, 0, -1, 1)
    dy = (1, -1, 0, 0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= 10:
            continue
        elif m[nx][ny] == num:
            cnt += 1
            dfs(num, nx, ny, cnt)

    return cnt


for i in range(n):
    for j in range(10):
        cnt = 0
        if m[i][j] != 0 and visited[i][j] == 0:
            num = dfs(m[i,j], i, j, cnt)

            if num >= 3:
                pass






