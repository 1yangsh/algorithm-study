n = int(input())

data = [int(input()) for _ in range(n)]
data.sort()

result = 0
data1 = []
data2 = []

for d in data:
    if d <= 0:
        data1.append(d)
    else:
        data2.append(d)


if len(data1) % 2 != 0:
    result += data1.pop()
    for i in range(0, len(data1) - 1, 2):
        result += data1[i] * data1[i + 1]
else:
    if data1:
        for i in range(0, len(data1) - 1, 2):
            result += data1[i] * data1[i + 1]

if len(data2) % 2 != 0:
    result += data2.pop(0)
    for i in range(0, len(data2) - 1, 2):
        result += data2[i] * data2[i + 1]
    result += round(data2.count(1) / 2)

else:
    if data2:
        if data2[0] == 1:
            for i in range(0, len(data2) - 1, 2):
                result += data2[i] * data2[i + 1]
            result += round(data2.count(1) / 2)
        else:
            for i in range(0, len(data2) - 1, 2):
                result += data2[i] * data2[i + 1]

print(result)

        
