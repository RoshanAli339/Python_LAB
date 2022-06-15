o1 = int(input("Enter operand 1: "))
o2 = int(input("Enter operand 2: "))
op = input("Enter an operator: ")

if op == '+':
    print(f"{o1} + {o2} = ", o1+o2)
elif op == '-':
    print(f"{o1} - {o2} = ", o1-o2)
elif op == '*':
    print(f"{o1} * {o2} = ", o1*o2)
elif op == '/':
    print(f"{o1} / {o2} = ", o1/o2)
elif op == '%':
    print(f"{o1} % {o2} = ", o1%o2)
else:
    print("Invalid operator")