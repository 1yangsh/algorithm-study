
def new_array(n):
    return [[False] * 10 for _ in range(n)]

n, k = map(int, input().split())

m = [list(input()) for _ in range(n)]

ck = new_array[n]
ck2 = new_array[n]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0  or yy < 0 or xx >= n or yy >= 10:
            continue
        if ck[xx][yy] or m[x] != m[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret







