## 우주선 발사 카운트다운
def countDown(n):
    if n == 0:
        print("발사!!")
    else:
        print(n)
        countDown(n-1)

countDown(10)