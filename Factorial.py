def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    user_input = int(input("Enter number to calculate factorial: "))
    if user_input < 0:
        print("Enter positive Number")
    else:
        result = factorial(user_input)
        print(f"The factorial of {user_input} is: {result}")
except ValueError:
    print("!! Invalid input !!")
