n = int(input())
result = list()

for _ in range(n):
    a, b = input().split()
    b = list(b)
    b.pop(int(a) - 1)
    result.append(b)


for r in result:
    print(''.join(r))