
s = input()
tmp = ""
ck = False

for i in s:
    if i == ' ':
        if not ck:
            print(tmp[::-1], end=" ")
            tmp = ""
        else:
            print(' ', end='')
    elif i == '<':
        print(tmp[::-1], end='')
        tmp = ""
        ck = True
        print("<", end='')
    elif i == '>':
        ck = False
        print(">", end='')
    else:
        if not ck:
            tmp += i
        else:
            print(i, end="")

if len(tmp) != 0:
    print(tmp[::-1])

