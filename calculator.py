import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm input must be positive."
    return math.log(x, base)

def modulus(x, y):
    return x % y

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number doesn't exist."
    return math.factorial(int(x))

def trigonometry(x, func):
    if func == "sin":
        return math.sin(math.radians(x))
    elif func == "cos":
        return math.cos(math.radians(x))
    elif func == "tan":
        return math.tan(math.radians(x))
    else:
        return "Error! Invalid trigonometric function."

def print_menu():
    print("\nSelect an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square root (√)")
    print("7. Logarithm (log)")
    print("8. Modulus (%)")
    print("9. Factorial (fact)")
    print("10. Trigonometry (sin, cos, tan)")

def main():
    while True:
        print_menu()
        choice = input("Enter choice (1-10) or 'exit' to quit: ")

        if choice == 'exit':
            print("Exiting the calculator.")
            break

        if choice == '1':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {add(x, y)}")

        elif choice == '2':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {subtract(x, y)}")

        elif choice == '3':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {multiply(x, y)}")

        elif choice == '4':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {divide(x, y)}")

        elif choice == '5':
            x = float(input("Enter base number: "))
            y = float(input("Enter exponent: "))
            print(f"Result: {power(x, y)}")

        elif choice == '6':
            x = float(input("Enter number to find square root: "))
            print(f"Result: {sqrt(x)}")

        elif choice == '7':
            x = float(input("Enter number: "))
            base = float(input("Enter base (default 10): ") or 10)
            print(f"Result: {logarithm(x, base)}")

        elif choice == '8':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {modulus(x, y)}")

        elif choice == '9':
            x = float(input("Enter number for factorial: "))
            print(f"Result: {factorial(x)}")

        elif choice == '10':
            x = float(input("Enter angle in degrees: "))
            func = input("Enter trigonometric function (sin, cos, tan): ").lower()
            print(f"Result: {trigonometry(x, func)}")

        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()
