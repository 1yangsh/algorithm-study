from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

result = 0

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            empty.append((i, j))
        elif data[i][j] == 2:
            virus.append((i, j))


# 벽을 세울 수 있는 경우의수 조합(중복허용 X) 로 구함
options = list(combinations(empty, 3))


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(array):
    q = deque([])
    for i in array:
        q.append(i)
        c_data[i[0]][i[1]] == 2

    while q:
        x, y = q.popleft()
        c_data[x][y] = 2
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif c_data[nx][ny] == 0:
                q.append((nx, ny))



for i,j,k in options:
    c_data = copy.deepcopy(data)
    c_data[i[0]][i[1]] = 1
    c_data[j[0]][j[1]] = 1
    c_data[k[0]][k[1]] = 1

    bfs(virus)

    result = max(result, sum([i.count(0) for i in c_data]))

    
print(result)

