x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

print(f"Bitwise AND: {x} & {y}: ", x&y)
print(f"Bitwise OR: {x} | {y}: ", x|y)
print(f"Bitwise NOT: ~{x}: ", ~x)
print(f"Bitwise XOR: {x} ^ {y}: ", x^y)
print(f"Bitwise right shift: {x} >> {y}: ", x>>y)
print(f"Bitwise left shift: {x} << {y}: ", x<<y)
