def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

lower_value = int(input("Enter the Lowest Range Value: "))
upper_value = int(input("Enter the Upper Range Value: "))

print("The Prime Numbers in the range are:")
for num in range(lower_value, upper_value + 1):
    if is_prime(num):
        print(num)
