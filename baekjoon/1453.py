n = int(input())

data = list(map(int, input().split()))


print(len(data) - len(set(data)))