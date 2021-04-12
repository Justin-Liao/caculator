import random

arr = [random.randint(0, 100) for i in range(10)]


def selectionSort(arr=list):
    for m in range(len(arr)):
        low = m
        for n in range(len(arr)-m):
            if arr[n+m] < arr[low]:
                low = n+m
        arr[m], arr[low] = arr[low], arr[m]
    return arr


print(arr)
print(selectionSort(arr))
