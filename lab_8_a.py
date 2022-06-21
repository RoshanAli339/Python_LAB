import gc


def gcd(n1, n2):
    if n2 != 0:
        return gcd(n2, n1 % n2)
    else:
        return n1


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(f"GCD of {n1} and {n2}: ", gcd(n1, n2))
