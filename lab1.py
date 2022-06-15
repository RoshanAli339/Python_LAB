from math import *
#importing cmath for complex numbers
import cmath

print("Enter the coefficients of a quadratic equation: ")
a = float(input("Coefficient a: "))
b = float(input("Coefficient b: "))
c = float(input("Coefficient c: "))

det = b**2 - (4*a*c)

r1 = 0
r2 = 0

if det == 0:
    r1 = r2 = -b/(2*a)
    print("The roots are real and equal. Roots= ", r1)
elif det > 0:
    r1 = (-b + sqrt(det))/(2*a)
    r2 = (-b - sqrt(det))/(2*a)
    print(f"The roots are real and distinct. Root1 = {r1}  Root2 = {r2}")
else:
    r1 = (-b + cmath.sqrt(det))/(2*a)
    r2 = (-b - cmath.sqrt(det))/(2*a)
    print(f"The roots are imaginary. Root1 = {r1}   Root2 = {r2}")