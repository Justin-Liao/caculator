import random

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [2, 5]
t = num[result[0]]+num[result[1]]


def twoSum(arr, target):
    for first in range(len(arr)-1):
        for second in range(first + 1, len(arr)):
            if arr[first] + arr[second] == target:
                return [first, second]
    return []


print(num)
print(t)
print(result)

print(twoSum(num, t))
