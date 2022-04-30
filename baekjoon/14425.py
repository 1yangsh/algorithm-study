n, m = map(int, input().split())
data = {input() for _ in range(n)}
cnt = 0

for _ in range(m):
    string = input()
    if string in data:
        cnt += 1

print(data)

print(cnt)