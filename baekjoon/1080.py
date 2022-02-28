n, m = map(int, input().split())

a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]
ans = 0


def flip(x, y, a):
    for i in range(3):
        for j in range(3):
            a[x + i][y + j] ^= 1


for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            flip(i, j, a)
            ans += 1


print(ans if a == b else -1)