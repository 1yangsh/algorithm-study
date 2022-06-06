from collections import defaultdict

data = list()

while True:
    try:
        data.append(input())
    except:
        break

data.sort()


wdict = defaultdict(int)
for word in data:
    wdict[word] += 1

# wdict = dict(wdict)

length = len(data)
for k, v in wdict.items():
    # print(f"{k} {round(v / length * 100, 4)}")
    print("%s %.4f" % (k, v / length * 100))
