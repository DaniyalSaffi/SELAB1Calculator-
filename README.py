# SELAB1Calculator-
#Simple Calculator in Python
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero."

# Main program
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    print("Result:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result:", result)
elif choice == '4':
    result = divide(num1, num2)
    print("Result:", result)
else:
    print("Invalid input. Please enter a valid choice (1-4).")