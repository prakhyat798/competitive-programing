A = int(input("Enter base (A): "))
B = int(input("Enter exponent (B): "))

result = 1
for i in range(B):
    result = result * A

print("A^B =", result)
