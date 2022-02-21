n = int(input())

result = []

for _ in range(n):
    data = sorted(list(map(int, input().split())))

    length = len(set(data))
    if length == 1:
        result.append(50000 + data[0] * 5000)
    elif length == 2:
        if data[1] == data[2]:
            result.append(10000 + data[1] * 1000)
        else:
            result.append(2000 + data[0] * 500 + data[-1] * 500)
    elif length == 3:
        if data[2] == data[3]:
            result.append(1000 + data[3] * 100)
        else:
            result.append(1000 + data[1] * 100)
    else:
        result.append(data[-1] * 100)

print(max(result))