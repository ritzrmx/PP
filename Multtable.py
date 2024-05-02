def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

while True:
    print("\nMenu:")
    print("1. Multiplication Table Generator")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            num = int(input("Enter the number for multiplication table: "))
            multiplication_table(num)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '2':
        exit()
    else:
        print("!! Invalid choice !!")
