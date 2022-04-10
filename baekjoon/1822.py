n, m = map(int, input().split())
data = dict()
for i in map(int, input().split()):
    if i not in data.keys():
        data[i] = 1
    else:
        data[i] += 1
for j in map(int, input().split()):
    if j in data.keys():
        data[j] = 0

cnt = 0
result = []
for key, value in sorted(data.items()):
    if value == 1:
        cnt += 1
        result.append(key)

print(cnt)
for r in result:
    print(r, end=" ")