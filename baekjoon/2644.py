import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
m = int(input())
data = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)


def dfs(x, cnt):
    cnt += 1
    visited[x] = True

    for i in data[x]:
        if not visited[i]:
            if i == y:
                print(cnt)
                sys.exit()
            dfs(i, cnt)

    cnt -= 1


cnt = 0
dfs(x, cnt)
cnt = 0
dfs(y, cnt)
print(-1)