## 두 배열의 원소 교체
n, k = map(int, input().split())
a=[]
b=[]
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(a, b)

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break

print(sum(a))
