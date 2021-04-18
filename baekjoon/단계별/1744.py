n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)
print(data)
sum = 0
for i in range(len(data)-1):
    j = i + 1
    if data[j] <= 1:
        sum += i
    elif data[j] > 1:
        sum += (data[i] * data[j])
        data[j] = 1
    else:
        sum += i
    print(i, sum)

print(sum)