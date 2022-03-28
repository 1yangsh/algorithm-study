import sys

a, b = map(int, input().split())

data = []
for i in range(1, b + 1):
    for j in range(0, i):
        data.append(i)
        if len(data) == b:
            print(sum(data[a-1:b+1]))
            sys.exit()
