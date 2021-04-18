## 별 모양 출력 재귀 호출로 구현

def printStar(n):
    if n > 0:
        printStar(n-1)
        print("★" * n)

printStar(5)