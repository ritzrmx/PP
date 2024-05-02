def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2

def exponent(num1, num2):
    return num1 ** num2

while True:
    print("Select an operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        if choice == '1':
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter second number: "))
            print(add(num1, num2))
    
        elif choice == '2':
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter second number: "))
            print(sub(num1, num2))
        
        elif choice == '3':
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter second number: "))
            print(multiply(num1, num2))
    
        elif choice == '4':
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter second number: "))
            print(divide(num1, num2))
    
        elif choice == '5':
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter second number: "))
            print(exponent(num1, num2))
            
    else:
        print("Invalid input. Please enter a valid choice (1-9).")

    another_calculation = input("Do you want to perform another operation? (y/n): ")

    if another_calculation.lower() != 'y':
        print("Thank you!")
        break









#codedbyRMX