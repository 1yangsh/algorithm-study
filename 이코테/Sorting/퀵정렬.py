# 퀵 정렬

data = [3, 7, 8, 1, 5, 9, 6, 10, 2, 4]


def quickSort(data):
    n = len(data)

    if n <= 1:
        return data
    else:
        pivot = data[0]
        less = [x for x in data[1:] if x <= pivot]  # pivot 보다 작은 값
        greater = [x for x in data[1:] if x > pivot]  # pivot 보다 큰 값
        return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort(data))