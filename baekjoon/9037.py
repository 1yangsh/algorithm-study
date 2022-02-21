test = int(input())

result = []

def change_even(n):
    if n % 2 != 0:
        return n + 1
    else:
        return n


for _ in range(test):
    kids = int(input())
    candy = list(map(int, input().split()))
    cnt = 0

    for i in range(kids):
        candy[i] = change_even(candy[i])

    
    if min(candy) == max(candy):
        result.append(cnt)
    
    else:

        while True:
            result_candy = [i // 2 for i in candy]
            half_candy = [result_candy[-1]] + result_candy[:-1]
            
            
            candy = [x + y for x, y in zip(result_candy, half_candy)]

            for i in range(kids):
                candy[i] = change_even(candy[i])

            cnt += 1
            if min(candy) == max(candy):
                break
        result.append(cnt)
        


for r in result:
    print(r)
            
        