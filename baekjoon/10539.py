n = int(input())

data = list(map(int, input().split()))

array = []

for i in range(n):
    array.append(data[i] * (i + 1) - sum(array))

for j in array:
    print(j, end=" ")
    