import sys

n = int(input())

data = [int(input()) for _ in range(n)]

visited = [False] * (n + 1)


result = []
now = 1
for d in data:
    if d >= now:
        for i in range(now, d + 1):
            if visited[i] == False:
                result.append('+')
            now = i
        if visited[now] == True:
            print("NO")
            sys.exit()
        result.append('-')
        visited[now] = True
        
    else:
        for i in range(now - 1, d, -1):
            if visited[i] == False:
                result.append('-')
                visited[i] = True
            now = i
        now -= 1
        if visited[now] == True:
            print("NO")
            sys.exit()
        result.append('-')
        visited[now] = True
        



for r in result:
    print(r)

