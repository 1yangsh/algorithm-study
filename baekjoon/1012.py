import sys
sys.setrecursionlimit(100000)

case = int(input())
result = []



def dfs(x, y):
    array[x][y] = 2
    dx = (-1, 1, 0, 0 )
    dy = (0, 0, -1, 1)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        elif array[nx][ny] == 1:
            dfs(nx, ny)
    


for _ in range(case):
    m, n, k = map(int, input().split())
    array = [[0] * m  for _ in range(n)]
    cnt = 0
    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y] = 1

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 1:
                dfs(i, j)
                cnt += 1

    result.append(cnt)



for i in result:
    print(i)


