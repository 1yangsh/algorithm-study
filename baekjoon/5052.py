import sys
input = sys.stdin.readline

test = int(input())

def check_num(data, n):
    for i in range(n - 1):
        length = len(data[i])
        if data[i] == data[i + 1][:length]:
            return "NO"
        
    return "YES"


for _ in range(test):
    n = int(input())

    data = [input().rstrip() for _ in range(n)]
    data.sort()

    print(check_num(data, n))
