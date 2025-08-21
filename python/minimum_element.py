A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

if A <= B and A <= C:
    print("Minimum is", A)
elif B <= A and B <= C:
    print("Minimum is", B)
else:
    print("Minimum is", C)
