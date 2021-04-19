## 떡볶이 떡 문제

n, m = map(int, input().split())
dduk = list(map(int, input().split()))

start = 0
end = max(dduk)
sum = 0
while(sum >= m):
    mid = (start + end) // 2
    for i in dduk:
        if i > mid:
            sum = i - mid
