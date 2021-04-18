n = int(input())
ary1 = list(map(int, input().split()))
ary2 = list(map(int, input().split()))

ary1.sort()
ary2.sort(reverse=True)
sum = 0
for i in range(len(ary1)):
    sum += (ary1[i] * ary2[i])

print(sum)
