## Selection Sort

def selectionSort(ary):
    n = len(ary)
    for i in range(n-1):
        minIdx = i
        for j in range(i+1, n):
            if ary[minIdx] > ary[j]:
                minIdx = j
        # 두 값을 바꾸기
        ary[i], ary[minIdx] = ary[minIdx], ary[i]

    return ary


dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
print('정렬 전-->', dataAry)
selectionSort(dataAry)
print('정렬 후-->', dataAry)