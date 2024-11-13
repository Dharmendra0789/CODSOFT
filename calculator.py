# Function to perform calculation on basic operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2 #addition
    elif operation == '-':
        return num1 - num2 #substraction
    elif operation == '*':
        return num1 * num2 #multiplication
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed." #division
        return num1 / num2
    else:
        return "Invalid operation."

# Main program
try:
    #user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform calculation and display the result
    result = calculate(num1, num2, operation)
    print("Result:", result)

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
