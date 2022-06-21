def fib(a):
    if a <= 1:
        return a
    return fib(a - 1) + fib(a - 2)


n = int(input('Enter number of terms: '))
for i in range(0, n+1):
    print(fib(i), end=', ')
