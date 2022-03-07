from collections import deque


test = int(input())

directions = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

def bfs(x, y, cnt):
    q = deque([(x, y, cnt)])

    if (des_x, des_y) == (x, y):
        return cnt

    while q:
        x, y, tt = q.popleft()
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if (des_x, des_y) == (nx, ny):
                return tt + 1
            if nx < 0 or ny < 0 or nx >= l or ny >= l or m[nx][ny] == 1:
                continue
            else:
               q.append((nx, ny, tt + 1))
               m[nx][ny] = 1




for _ in range(test):
    l = int(input())
    m = [[0] * l for _ in range(l)]

    x, y = map(int, input().split())
    des_x, des_y = map(int, input().split())

    
    print(bfs(x, y, 0))
