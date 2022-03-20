from itertools import combinations

test = int(input())
result = []

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

for _ in range(test):
    n, m = map(int, input().split())

    result.append(factorial(m) // (factorial(n) * factorial(m - n)))

for r in result:
    print(r)