def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

try:
    user_input = int(input("Enter a number: "))
    check_even_odd(user_input)
except ValueError:
    print("Invalid input! Please enter a valid number.")
