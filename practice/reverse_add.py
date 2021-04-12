import random

l1 = [random.randint(1, 9), random.randint(
    1, 9), random.randint(1, 9), random.randint(1, 9)]
l2 = [random.randint(1, 9), random.randint(
    1, 9), random.randint(1, 9)]


def func1(list1=[], list2=[]):
    ansArr = [int(num) for num in str(reverse(list1)+reverse(list2))]
    ans = [int(num) for num in str(reverse(ansArr))]
    return ans


def reverse(arr):
    num = 0
    for index in range(len(arr)):
        num += arr[index]*(10**index)
    return num


def func2(list1=[], list2=[]):
    if len(list1) > len(list2):
        list1, list2 = list2, list1

    ans = []
    carry = 0
    for index in range(len(list1)):
        add = (list1[index]+list2[index]) + carry
        ans.append(add % 10)
        carry = add // 10

    for index in range(len(list1), len(list2)):
        add = (list2[index]) + carry
        ans.append(add % 10)
        carry = add // 10

    if (carry):
        ans.append(carry)

    return ans


print(l1)
print(l2)
# print(func1(l1, l2))
print(func2(l1, l2))
