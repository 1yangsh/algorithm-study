import sys
n = sys.stdin.readline()
line = int(sys.stdin.readline())


data = [[input().split()] for _ in range(line)]

print(data)
cnt = 0


visited = [0] * 9
print(visited)

