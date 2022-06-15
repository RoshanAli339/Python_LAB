r1 = int(input("Enter number of rows in matrix A: "))
c1 = int(input("Enter number of columns in matrix A: "))

r2 = int(input("Enter number of rows in matrix B: "))
c2 = int(input("Enter number of columns in matrix B: "))

# number of columns of first matrix should be equal to number of rows of second matrix
if c1 != r2:
    print("Matrix multiplication is not possible!")
    exit(1)

a = [[0 for i in range(c1)] for i in range(r1)]
b = [[0 for i in range(c2)] for i in range(r2)]

print("Enter the elements of matrix A: ")
for i in range(r1):
    for j in range(c1):
        ele = int(input())
        a[i].insert(j, ele)

print("Enter the elements of matrix B: ")
for i in range(r1):
    for j in range(c1):
        ele = int(input())
        b[i].insert(j, ele)

c = [[0 for i in range(r1)] for i in range(c2)]
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            c[i][j] = a[i][k] + b[k][j]

print("Matrix A x Matrix B: ")
for i in range(r1):
    for j in range(c2):
        print(c[i][j], end=' ')
    print()
