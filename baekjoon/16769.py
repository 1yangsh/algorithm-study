capacity = []
milk = []

for i in range(3):
    a, b = map(int, input().split())
    capacity.append(a)
    milk.append(b)

for i in range(100):
    idx = i % 3
    next = (i + 1) % 3 

    if milk[idx] + milk[next] <= capacity[next]:
        milk[next] += milk[idx]
        milk[idx] = 0

    else:
        milk[idx] = (milk[idx] + milk[next]) - capacity[next]
        milk[next] = capacity[next]


for i in milk:
    print(i)
        