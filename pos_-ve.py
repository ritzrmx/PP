def check_num(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

user_input = input("Enter a number: ")

try:
    number = int(user_input)
    check_num(number)
except ValueError:
    print("Invalid input! Please enter a valid number.")

        
        
        
        
        
        
        
#codedbyRMX
