def selectionSort(ary):
    n = len(ary)
    for i in range(n-1):
        minIdx = i
        for j in range(i, n):
            if ary[minIdx] > ary[j]:
                minIdx = j
        ary[i], ary[minIdx] = ary[minIdx], ary[i]

dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
print('정렬 전-->', dataAry)
selectionSort(dataAry)
print('정렬 후-->', dataAry)