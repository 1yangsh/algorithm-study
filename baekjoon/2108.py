n = int(input())

data = [int(input()) for _ in range(n)]
data.sort()

cnt = {}


if len(data) != 1:
    print(round(sum(data) / len(data))) # 산술평균
    print(data[int((n - 1) / 2)]) # 중앙값

    for i in data:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1

    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
    print(data[-1] - data[0]) # 범위
else:
    print(data[0])
    print(data[0])
    print(data[0])
    print(0)