r, c = map(int, input().split())

map = [list(input()) for i in range(r)]


def check_safe(r, c, map):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(r):
        for j in range(c):
            if map[i][j] == 'W':
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    if map[nx][ny] == 'S':
                        return 0
    return 1

result = check_safe(r, c, map)
if result == 0:
    print(result)
else:
    print(result)
    for i in range(r):
        for j in range(c):
            if map[i][j] not in 'SW':
                map[i][j] = 'D'


    for i in map:
        print(''.join(i))
