n = int(input())

result = 0

def cycle(num):
    length = len(num)

    if length == 1:
        num = '0' + num

    next = str(int(num[0]) + int(num[1]))

    if len(next) == 1:
        next = num[1] + next
    else:
        next = num[1] + next[1]

    return next


t = n
while True:
    next = cycle(str(t))
    result += 1


    if int(next) == n:
        print(result)
        break

    t = next

