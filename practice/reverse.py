import random


def reverse(arr):
    for index in range(len(arr)//2):
        arr[index], arr[-index-1] = arr[-index-1], arr[index]


arr1 = [random.randint(0, 100) for i in range(10)]
arr2 = arr1.copy()

print(arr1)

reverse(arr1)
print(arr1)

arr2.reverse()
print(arr2)
