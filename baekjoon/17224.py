n, l, k = map(int, input().split())


data = [list(map(int, input().split())) for _ in range(n)]

score = 0

for i in range(len(data)):
    if l >= data[i][1]:
        score += 140
        k -= 1
        if k == 0:
            break

if k != 0:
    for i in range(len(data)):
        if l < data[i][1] and l >= data[i][0]:
            score += 100
            k -= 1
            if k == 0:
                break


print(score)