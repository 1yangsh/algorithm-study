data = list(map(int, input().split()))
data.sort()

def is_unique(n):
    return len(set(n))


case = is_unique(data)

if case == 1:
    print(10000 + data[1] * 1000)
elif case == 2:
    print(1000 + data[1] * 100)
else:
    print(data[-1] * 100)


