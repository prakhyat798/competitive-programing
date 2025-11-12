def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return "invalid"
num1 = 10
num2 = 5
opr = '*'
print(calc(num1, num2, opr))