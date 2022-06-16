from math import *


def ncr(n, r):
    return int(factorial(n)/(factorial(n-r) * factorial(r)))


for i in range(0, 5):
    for j in range(1, 5-i+1):
        print(end=' ')

    for j in range(0, i+1):
        print(ncr(i, j), end=' ')
    print()
