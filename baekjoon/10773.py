n = int(input())

result = []

for _ in range(n):
    data = int(input())
    if data != 0:
        result.append(data)
    else:
        result.pop()

print(sum(result))