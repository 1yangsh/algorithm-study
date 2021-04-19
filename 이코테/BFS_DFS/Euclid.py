# 재귀함수를 이용한 유클리드 호제법으로 최대공약수(GCD) 구하기
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))