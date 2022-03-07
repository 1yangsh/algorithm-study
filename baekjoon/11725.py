import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

data = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)


visited = [False] * (n + 1)
result = {}

def dfs(x, visited):
    visited[x] = True

    for d in data[x]:
        if not visited[d]:
            result[d] = x
            dfs(d, visited)


dfs(1, visited)

for i in range(2, n + 1):
    print(result[i])