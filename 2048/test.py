
def bsearch(num, arr):
    left = 0
    right = len(arr)-1
    while right >= left:
        mid = (left + right) // 2
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


data = [2, 4, 24, 43, 51, 68, 86, 92, 100]

print("1'position is " + str(bsearch(1, data)))
print("2'position is " + str(bsearch(2, data)))
print("68'position is " + str(bsearch(68, data)))
print("99'position is " + str(bsearch(99, data)))
print("100'position is " + str(bsearch(100, data)))
print("101'position is " + str(bsearch(101, data)))
