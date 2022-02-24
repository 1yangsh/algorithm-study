
data = []

for i in range(1, 10001):
    n = str(i)
    m = i
    for j in range(len(n)):
        m += int(n[j])

    data.append(m)

for i in range(1, 10001):
    if i not in data:
        print(i)