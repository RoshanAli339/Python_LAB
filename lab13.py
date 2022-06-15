a = [78,65,22,66,99]

print('The elements of the list are: ', a)

x = int(input("Enter a number to append: "))
a.append(x)

print("After appending the list is: ", a)

b = [5,15,66,74]
print('List B: ', b)
a.extend(b)
print('After extending with list B the list A is: ', a)

x = int(input('Enter an element to insert: '))
pos = int(input('Enter the position to insert the element in the list: '))
a.insert(pos, x)
print('After inserting the list is: ', a)

x = int(input('Enter an element to find its index: '))
print(f'The first appearence of {x} is: ', a.index(x))

a.sort()
print('After sorting the list is: ', a)
