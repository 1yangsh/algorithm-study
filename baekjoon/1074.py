n, r, c = map(int, input().split())


# Z : 0,0으ㄹ 기준으로 x, y의 숫자
def Z(sz, x, y):
    if sz == 1:
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if x < sz * (i+1) and y < sz * (j+1):
                return (i*2+j) * sz * sz + Z(sz,x-sz*i, y-sz*j)




print(Z(2**n, r, c))