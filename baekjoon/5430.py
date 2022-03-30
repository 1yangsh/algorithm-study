n = int(input())

for _ in range(n):
    func = input()
    length = int(input())

    if length > 0:
        data = list(map(int, input()[1:-1].split(',')))
        try:
            j = 0
            for i in func:
                if i == 'R':
                    if j == 0:
                        j = -1
                    else:
                        j = 0
                elif i == 'D':
                    data.pop(j)
            if j == 0:
                print(str(data).replace(', ', ','))
            else:
                print(str(data[::-1]).replace(', ', ','))
        except:
            print("error")
    else:
        input()
        data = []
        if 'D' in func:
            print("error")
        else:
            print(data)


