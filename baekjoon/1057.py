import sys

n, k, l = map(int, input().split())


def get_next_num(n):
    if n % 2 == 1:
        return n // 2 + 1
    return n // 2


game = [i + 1 for i in range(n)]

i = 1

while True:
    last_num = None
    game = [a + 1 for a in range(len(game))]
    if len(game) == 1:
        print(-1)
        exit()
    elif len(game) == 2:
        print(i)
        exit()


    if len(game) % 2 == 0:
        game = [(a, b) for a, b in zip(game[::2], game[1::2])]
    else:
        last_num = game[-1]
        game = [(a, b) for a, b in zip(game[::2], game[1::2])]

    for a, b in game:
        if (a == k and b == l) or (a == l and b == k):
            print(i)
            exit()
            
    k, l = get_next_num(k), get_next_num(l)
    i += 1

    if last_num:
        game.append(last_num)
    