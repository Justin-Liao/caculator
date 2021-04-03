arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def MybSearch(arr, value, min, max):
    minNumber = min
    maxNumber = max
    middle = int((minNumber+maxNumber)/2)
    if value == arr[middle]:
        return middle
    if value == arr[maxNumber]:
        return maxNumber
    if value == arr[minNumber]:
        return minNumber
    if value > arr[middle]:
        minNumber = middle
        return MybSearch(arr, value, minNumber, maxNumber)
    if value < arr[middle]:
        maxNumber = middle
        return MybSearch(arr, value, minNumber, maxNumber)


print(MybSearch(arr, 3, 0, len(arr)-1))
