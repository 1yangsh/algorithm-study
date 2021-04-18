## 이진탐색
# 정렬된 데이터를 사용해야 한다

def binSearch(ary, fData):
    pos =-1
    start = 0
    end = len(ary) - 1

    while (start <= end):
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return pos



dataAry = [50, 105, 120, 150, 162, 168, 177, 188]
findData = 162

position = binSearch(dataAry, findData)
if position == -1:
    print("없어요")
else:
    print(dataAry[position])