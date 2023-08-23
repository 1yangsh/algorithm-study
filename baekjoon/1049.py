n, m = map(int, input().split())

prices = [list(map(int, input().split())) for _ in range(m)]
min_set_price = min(map(lambda x: x[0], prices))
min_each_price = min(map(lambda x: x[1], prices))

if n < 7:
    print(min(n * min_each_price, min_set_price))
else:
    if min_set_price <= min_each_price:
        if not n % 6:
            print((n // 6 * min_set_price))
        else:
            print((n // 6 * min_set_price) + min_set_price)
    elif min_each_price * 6 <= min_set_price:
        print(n * min_each_price)
    else:
        print((n // 6 * min_set_price) + (min(n % 6 * min_each_price, min_set_price)))
