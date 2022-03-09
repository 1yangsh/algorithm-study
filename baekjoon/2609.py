def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)


a, b = map(int, input().split())

print(gcd(a, b))
print((a * b) // gcd(a, b))