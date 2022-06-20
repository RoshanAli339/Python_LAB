def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


a = int(input("Enter number of terms: "))
for i in range(0, a):
    print(fib(i), end=' ')
