from collections import deque

m, n, h = map(int, input().split())


array = []
for _ in range(h):
    data = []
    for _ in range(n):
        i = list(map(int, input().split()))
        data.append(i)

    array.append(data)


directions = ((1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

def bfs(v):
    cnt = 0
    q = deque([])
    for a in v:
        q.append(a)

    length = len(v)
    re_length = 0

    while q:
        z, y, x = q.popleft()

        for dx, dy, dz in directions:
            nz = z + dz
            ny = y + dy
            nx = x + dx

            if nz < 0 or ny < 0 or nx < 0 or nx >= m or ny >= n or nz >= h:
                continue
            if array[nz][ny][nx] == 0:
                q.append((nz, ny, nx))
                array[nz][ny][nx] = 1
                re_length += 1
        length -= 1
        if length == 0:
            cnt += 1
            length = re_length
            re_length = 0

    return cnt
    

start = 0
for i in range(h):
        for j in range(n):
            for k in range(m):
                if array[i][j][k] == 0:
                    start = 1


if start== 1:
    res = []
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if array[i][j][k] == 1:
                    res.append((i, j, k))

    cnt = bfs(res)

    start = 0

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if array[i][j][k] == 0:
                    start = 1

    if start == 0:
        print(cnt - 1)
    else:
        print(-1)

else:
    print(0)