n, m = map(int, input().split())
a, b = input().split()

alphabet = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

min_len = min(n, m)

ab = ''
for i in range(min_len):
    ab += a[i] + b[i]

ab += a[min_len:] + b[min_len:]

lst = [alphabet[int(ord(i) - ord('A'))] for i in ab]

def calculate(lst):
    result = []
    for i in range(len(lst) - 1):
        num = lst[i] + lst[i + 1]
        if num >= 10:
            num -= 10
        result.append(num)

    return result

while len(lst) != 2:
    lst = calculate(lst)

if lst[0] != 0:
    print(str(lst[0])+str(lst[1])+'%')
else:
    print(str(lst[1])+'%')