fib = [1, 1, 2, 3, 5, 8, 13, 21, 34]


def fib(n):
    num1 = 1
    num2 = 1
    if n == 1 or n == 2:
        return num1
    for i in range(n-2):
        num1, num2 = num2, num1+num2
    return num2


for i in range(10):
    print(fib(i+1))
