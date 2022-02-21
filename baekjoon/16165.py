n, m = map(int, input().split())

g_group = {}
for _ in range(n):
    name = input()
    a = int(input())
    members = [input() for _ in range(a)]
    g_group[name] = members

for _ in range(m):
    q = input()
    num = int(input())

    if num == 1:
        for k, v in g_group.items():
            if q in v:
                print(k)
                break
    else:
        for i in sorted(g_group[q]):
            print(i)
