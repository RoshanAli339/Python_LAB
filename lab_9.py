def perm(start, end=[]):
    if len(start) == 0:
        print(end)
    else:
        for i in range(len(start)):
            perm(start[:i] + start[i+1:], end+start[i:i+1])


ele = input('Enter space separated values: ')
a = ele.strip().split(' ')
a = [int(i) for i in a]

print("Before performing any operations the list is: ", a)

a.sort()
print('After sorting the elements of the list are: ', a)

x = int(input("Enter a number to search for in the list: "))
if x in a:
    print(x, " is present in the list")
else:
    print(x, " is not present in the list")

print("All possible permutations of the list: ")
perm(a)
