Number1 = int(input("Enter the first number : "))

Number2 = int(input("Enter the second number : "))

print("\n(1) - Addition (+)")
print("(2) - subtraction (-)")
print("(3) - Multiplication (*)")
print("(4) - Divistion (/)")
print("(5) - modulo (%)\n")
operator = int(input("Select the operation : "))

if operator == 1:
    result = Number1 + Number2
elif operator == 2:
    result = Number1 - Number2
elif operator == 3:
    result = Number1 * Number2
elif operator == 4:
    result = Number1 / Number2
elif operator == 5:
    result = Number1 % Number2
else:
    print("invalid Operator")

print(" result : ", result)
