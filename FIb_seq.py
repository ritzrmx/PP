n_terms = int(input("Enter the limit: "))

previous = 0
current = 1

if n_terms <= 0:
    print("Please enter a positive integer; the given number is not valid.")
elif n_terms == 1:
    print(f"1")
else:
    print("The Fibonacci sequence of the numbers is:")
    for _ in range(n_terms):
        print(previous)
        previous, current = current, previous + current