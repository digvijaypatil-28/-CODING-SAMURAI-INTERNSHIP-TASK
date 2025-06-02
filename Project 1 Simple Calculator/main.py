# Simple Calculator Program
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.
# It takes two numbers and an operation as input from the user and displays the result.
# Get user input for two numbers and the operation  

while True:
    
    num1=float(input("Enter first number: "))#take first input from user
    operation=input("Enter operation (+, -, *, /): ")#take operation from user
    num2=float(input("Enter second number: "))#take second input from user

    # Perform the calculation based on the operation

    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation. Please enter one of +, -, *, /.")                     
    choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break    