from math import sqrt
print("Select operation:")
print("+")
print("-")
print("*")
print("/")
print("sqrt")
print('%')

result = 0

while True:
    choice = input("Enter choice (+,-,*,/,sqrt,%): ")

    if choice in ('+', '-', '*', '/'):
        if result != 0:
            num1 = result
            num2 = float(input("Enter second number: "))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '+':
            result = num1 + num2
        elif choice == '-':
            result = num1 - num2
        elif choice == '*':
            result = num1 * num2
        elif choice == '/':
            result = num1 / num2
        print("Result:", result)

    elif choice == 'sqrt':
        num1 = result if result != 0 else float(input("Enter number: "))
        result = sqrt(num1)
        print("Result:", result)

    elif choice == '%':
        if result != 0:
            num1 = result
            num2 = float(input("Enter second number: "))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        result = num1 % num2
        print("Result:", result)

    else:
        print("Invalid input")

    again1 = input("Do you want to continue working with this result? (yes/no): ")
    if again1.lower() != 'yes':
        result = 0
        again2 = input("Do you want to do another calculation? (yes/no): ")
        if again2.lower() != 'yes':
            break