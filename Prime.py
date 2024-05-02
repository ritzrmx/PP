def is_prime(number):
    if number > 1:
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                print(f"{number} is not a prime number")
                break
        else:
            print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
user_input = int(input("Enter an input number: "))
is_prime(user_input)
