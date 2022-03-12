n, m = map(int, input().split())


result = []


def check(x, y):
    cnt = 0
    a = 'B'
    b = (x + y) % 2
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2 == b:
                if data[i][j] != a:
                    cnt += 1
            else:
                if data[i][j] == a:
                    cnt += 1
    cnt2 = 0
    a = 'W'
    b = (x + y) % 2
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2 == b:
                if data[i][j] != a:
                    cnt2 += 1
            else:
                if data[i][j] == a:
                    cnt2 += 1

    return min(cnt , cnt2)

data = list(input() for _ in range(n))

for i in range(n):
    for j in range(m):
        if (m - j) >= 8 and (n - i) >= 8:
            result.append(check(i, j))


print(min(result))