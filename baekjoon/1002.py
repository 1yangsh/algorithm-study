import math

n = int(input())
result = []

for _ in range(n):
    data = list(map(int, input().split()))

    if (data[0], data[1]) != (data[3], data[4]): # 두 점이 다를경우
        distance = math.sqrt(math.pow((data[4] - data[1]), 2) + math.pow((data[3] - data[0]), 2))

        if abs(data[2] + data[-1]) > distance and abs(data[2] - data[-1]) < distance:
            result.append(2)
        else:
            a = [data[2], data[-1], distance]
            a. sort()
            if a[0] + a[1] == a[2]:
                result.append(1)
            else:
                result.append(0)



    else: # 두 점이 같을 경우
        if data[2] != data[-1]:
            result.append(0)
        else:
            result.append(-1)


for r in result:
    print(r)

