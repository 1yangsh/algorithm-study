import copy
import sys
sys.setrecursionlimit(100000)

r, c = map(int, input().split())
data = [list(input()) for _ in range(r)]


visited = [False] * 26
# A = 65 / Z = 90

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, cnt, visited):
    global max_num
    visited[ord(data[x][y]) - 65] = True
    
    cnt += 1

    max_num = max(max_num, cnt)
 
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        elif visited[ord(data[nx][ny]) - 65] == True:
            continue
        else:
            dfs(nx, ny, cnt, visited)

    visited[ord(data[x][y]) - 65] = False
    cnt -= 1


max_num = 0
cnt = 0
dfs(0, 0, cnt, visited)

print(max_num)