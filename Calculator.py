def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Invalid choice!!!!"

def main():
    print("Hey User!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        # Options
        choice = input("Enter choice (1/2/3/4): ")

        # Crosschecking if it is ivalid
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input!! Try again!!")
            continue

        # To take numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Calculation
        if choice == '1':
            print(f"The Addition is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The Subtraction is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The Multiplication is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The Division is: {divide(num1, num2)}")

        # Check if the user wants to perform other calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            break

    print("Thank you for using the calculator!")

if __name__ == "__main__":
    main()