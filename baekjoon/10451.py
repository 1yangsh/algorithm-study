test = int(input())

result = []

for _ in range(test):
    n = int(input())
    data = list(map(int, input().split()))
    array = [[] for _ in range(n  + 1)]

    for i in range(1, len(data) + 1):
        array[i].append(data[i - 1])


    visited = [False] * (n + 1)

    def dfs(v, visited):
        visited[v] = True
        for i in array[v]:
            if not visited[i]:
                dfs(i, visited)


    cnt = 0
    for i in data:
        if not visited[i]:
            dfs(i, visited)
            cnt += 1
            
    result.append(cnt)

for i in result:
    print(i)


    