import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

maps = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)


def dfs(v, visied):
    visited[v] = True

    for i in maps[v]:
        if visited[i] == False:
            dfs(i, visited)


visited = [False] * (n + 1)
count = 0
for i in range(1, n + 1):
    if visited[i] == False:
        dfs(i, visited)
        count += 1

print(count)