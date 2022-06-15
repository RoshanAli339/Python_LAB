ele = input("Enter the elements of the list: ")
a = ele.split(' ')
a = [int(i) for i in a]

# a = list(set(a))
f = []

for i in a:
    if i not in f:
        f.append(i)

print('The list after deleting duplicates is: ', f)
