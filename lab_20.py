a = [int(x) for x in input("Enter the elements: ").strip().split()]
f = []

for i in a:
    if i not in f:
        f.append(i)

print('The list after deleting duplicates is: ', f)
