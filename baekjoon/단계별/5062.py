t = int(input())
for _ in range(t):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(str, input().split())))
    print(data)
    ans = 1
    for i in range(len(data) - 1):
        for j in range(i+1, len(data)):
            if data[i][0] in [data[j][0][0:len(data[i][0])]]:
                ans = 0
                break
        if ans == 0:
            break
    if ans == 1:
        print("YES")
    else:
        print("NO")
