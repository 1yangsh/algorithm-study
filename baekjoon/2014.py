import copy
import heapq

k, n = map(int, input().split())

data = list(map(int, input().split()))
ans = copy.deepcopy(data)
ck = set()


heapq.heapify(ans)

cnt = 0

while cnt < n:
    i = heapq.heappop(ans)
    if i in ck:
        continue
    cnt += 1
    ck.add(i)

    for d in data:
        if i * d < 2 ** 32:
            heapq.heappush(ans, i * d)

print(i)

