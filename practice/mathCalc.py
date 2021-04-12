import math


def mathCalc(a, b, c):
    if (b*b-4*a*c) > 0:
        d = math.sqrt(b*b-4*a*c)
        a1 = (d-b)/(2*a)
        a2 = (d+b)/(2*a)
        return [a1, a2]
    if (b*b-4*a*c) == 0:
        a1 = (-b)/(2*a)
        return[a1]
    if (b*b-4*a*c) < 0:
        return[]


while True:
    A = int(input('a:'))
    B = int(input('b:'))
    C = int(input('c:'))

    print(mathCalc(A, B, C))
