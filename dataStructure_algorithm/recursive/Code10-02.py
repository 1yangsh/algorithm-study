def openBox():
    global count
    print("상자 열기")
    count -= 1
    if count == 0:
        print("반지 넣었음 ㅋㅋㅋ")
        return
    openBox()
    print("## 상자 닫기 ##")

count = 10

openBox()