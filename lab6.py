from math import *


def prime(n):
    flag = True
    for i in range(2, n//2+1):
        if n % i == 0:
            flag = False
            break
    if flag:
        print(n, " is a Prime number")
    else:
        print(n, " is not a Prime number")

def armstrong(n):
    sum = 0
    l = len(str(n))
    for i in str(n):
        sum += int(i)**l
    
    if sum == n:
        print(n, " is an Armstrong number")
    else:
        print(n, " is not an Armstrong number")

def strong(n):
    sum = 0
    for i in str(n):
        sum += factorial(int(i))
    if sum == n:
        print(n, " is a Strong number")
    else:
        print(n, " is not a Strong number")

def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    
    if sum == n:
        print(n, " is a Perfect number")
    else:
        print(n, " is not a Perfect number")


n = int(input("Enter a number: "))

print("1.Prime\n2.Armstrong\n3.Strong\n4.Perfect")
ch = input("Enter your choice: ")

if ch == 'Prime':
    prime(n)
elif ch == 'Armstrong':
    armstrong(n)
elif ch == 'Strong':
    strong(n)
elif ch == 'Perfect':
    perfect(n)
else:
    print("Invalid choice!")