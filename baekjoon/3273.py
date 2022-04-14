n = int(input())
data = list(map(int, input().split()))
x = int(input())
cnt = 0
num = [0] * (10000001)
for i in data:
    num[i] = 1

for i in data:
    if num[i] == 1 and num[x - i] == 1 and i != x - i:
        num[i], num[x - i] = 2, 2
        cnt += 1

print(cnt)
