r = int(input("Enter number of rows of matrix : "))
c = int(input("Enter number of columns of matrix: "))


mat = [[0 for i in range(c)] for i in range(r)]

print("Enter the elements of the matrix: ")
for i in range(r):
    for j in range(c):
        ele = int(input())
        mat[i].insert(j, ele)

mat2 = [[0 for i in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        mat2[i][j] = mat[j][i]


print("Transpose of given matrix: ")
for i in range(c):
    for j in range(r):
        print(mat2[i][j], end=' ')
    print()
