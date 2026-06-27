# Task 2: Simple Calculator

print("--- Basic Calculator ---")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    ans = num1 + num2
    print("Result:", ans)
elif op == '-':
    ans = num1 - num2
    print("Result:", ans)
elif op == '*':
    ans = num1 * num2
    print("Result:", ans)
elif op == '/':
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        ans = num1 / num2
        print("Result:", ans)
else:
    print("Invalid operator entered.")