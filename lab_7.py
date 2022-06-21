from math import *

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print('Floor value of a: ', floor(a))
print('Ceil value of b: ', ceil(b))
print('Absolute value of a: ', fabs(a))
print(f'{a} raised to the power {b}: ', pow(a, b))

x = int(input("Enter an integer to find its factorial: "))
print(f'Factorial of {a} is: ', factorial(x))

x = int(input("Enter a integer to find its ASCII equivalent character: "))
print(f"The ASCII equivalent of {x} is: ", chr(x))

x = input("Enter a character to find its ASCII value: ")
print(f"The ASCII value of \'{x}\' is: ", ord(x))

print(f"ID of \'{x}\' is: ", id(x))
print(f"Type of {x} is: ", type(x))
