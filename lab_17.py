d={'km':'kilometer', 'gm':'grams', 'lb':'pounds', 'w':'Watt', 'j':'joules'}


a = input("Enter a unit: ")
print(f"Value of {a} is: ", d.get(a))

print("The keys are: ", d.keys())

a = input("Enter a unit to pop out from the list: ")
x = d.pop(a)
print("The popped out value is: ", x)

a = input("Enter a unit to update the dict: ")
x = input("Enter the value to update with: ")
d.update({a: x})
print("The updated dictionary is: ", d)

print("The values are: ", d.values())

print("The key value pairs are: ", d.items())
