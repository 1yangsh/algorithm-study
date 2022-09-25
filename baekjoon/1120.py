a, b = input().split()

len_a = len(a)
len_b = len(b)


cnt = 0
result = 0
for i in range(len_b - len_a + 1):
    for j in range(len(a)):
        if a[j] == b[i + j]:
            cnt += 1
    result = max(cnt, result)
    cnt = 0

print(len_a - result)