import sys
sys.setrecursionlimit(100000)

r, c = map(int, input().split())

m = [list(input()) for _ in range(r)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, s, w):
    m[x][y] = '#'

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        else:
            if m[nx][ny] == 'o':
                s += 1
                s, w = dfs(nx, ny, s, w)
            elif m[nx][ny] == 'v':
                w += 1
                s, w = dfs(nx, ny, s, w)
            elif m[nx][ny] == '.':
                s, w = dfs(nx, ny, s, w)

    return (s, w)

result_s = 0
result_w = 0

for i in range(r):
    for j in range(c):
        s, w = 0, 0
        if m[i][j] == 'o':
            s += 1
            s, w = dfs(i, j, s, w)
            if s > w:
                result_s += s
            else:
                result_w += w
        elif m[i][j] == 'v':
            w += 1
            s, w = dfs(i, j, s, w)
            if s > w:
                result_s += s
            else:
                result_w += w
        elif m[i][j] == '.':
            s, w = dfs(i, j, s, w)
            if s > w:
                result_s += s
            else:
                result_w += w


print(result_s, result_w)


