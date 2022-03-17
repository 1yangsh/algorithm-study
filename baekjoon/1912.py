n = int(input())
data = list(map(int, input().split()))
result = []

dp = 0

if max(data) <= 0:
    print(max(data))
else:
    if n > 1:
        for d in data:
            if dp + d <= 0:
                dp = 0
                continue
            dp += d
            result.append(dp)
        print(max(result))
    else:
        print(max(data))
