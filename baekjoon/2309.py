from itertools import combinations

data = [int(input()) for _ in range(9)]

for i in combinations(data, 7):
    if sum(i) == 100:
        result = i
        break

for r in sorted(result):
    print(r)