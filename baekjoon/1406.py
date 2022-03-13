data = list(input())
n = int(input())


stack = []


for _ in range(n):
    inp = list(input().split())

    if inp[0] == 'L':
        if len(data) != 0:
            stack.append(data.pop())
    elif inp[0] == 'D':
        if len(stack) != 0:
            data.append(stack.pop())
    elif inp[0] == 'P':
        data.append(inp[1])
    else:
        if len(data) != 0:
            data.pop()


print(''.join(data + stack[::-1]))