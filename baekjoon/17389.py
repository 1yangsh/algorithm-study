n = int(input())
score = input()


result = 0
bonus = 0
for i in range(1, n + 1):
    if score[i - 1] == 'O':
        result += i + bonus
        bonus += 1
    else:
        bonus = 0

print(result)