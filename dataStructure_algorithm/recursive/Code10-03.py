# sumValue = 0
# for n in range(10, 0, -1):
#     sumValue += n
# print(sumValue)

def addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(10))
