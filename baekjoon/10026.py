import sys
import copy

sys.setrecursionlimit(100000)

n = int(input())

data = [list(input()) for _ in range(n)]
data2 = copy.deepcopy(data)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, v):
    data[x][y] = "V"

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        else:
            if data[nx][ny] == v:
                dfs(nx, ny, v)

def dfs2(x, y, v):
    data2[x][y] = "V"

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        else:
            if data2[nx][ny] == v:
                dfs2(nx, ny, v)


cnt = 0
for i in range(n):
    for j in range(n):
        if data[i][j] in ('R', 'B', 'G'):
            dfs(i, j, data[i][j])
            cnt += 1
print(cnt, end=' ')



cnt = 0
for i in range(n):
    for j in range(n):
        if data2[i][j] == 'R':
            data2[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if data2[i][j] in ('B', 'G'):
            dfs2(i, j, data2[i][j])
            cnt += 1
print(cnt)      

