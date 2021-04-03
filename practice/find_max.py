import random

arr = [random.randint(0, 10240) for i in range(1000)]


def mymax(arr):
    maxValue = arr[0]
    for x in arr:
        if maxValue < x:
            maxValue = x
    return maxValue


print("my max is : " + str(mymax(arr)))
print("max is: " + str(max(arr)))
