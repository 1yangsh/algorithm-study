## 선택정렬

array = [7, 5, 9 ,0 ,3 ,1, 6, 2, 4, 8]

def selectionSort(array):
    for i in range(len(array) - 1):
        min = i
        for j in range(i, len(array)):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array

print(selectionSort(array))