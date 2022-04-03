data = [input() for _ in range(8)]

cnt = 0

for i in range(8):
    for j in range(i % 2, 8, 2):
        if data[i][j] == 'F':
            cnt += 1

print(cnt)