import calendar

while True:
    print("\nCALENDAR PROGRAM")
    print("1. Display Calendar")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        yy = int(input("Enter YEAR: "))
        mm = int(input("Enter MONTH: "))
        
        if 1 <= mm <= 12 and yy > 0:
            print(calendar.month(yy, mm))
        else:
            print("Invalid input !! Please enter a valid mm & yy")

    elif choice == '2':
        exit()

    else:
        print("!! Invalid choice !!")



# import calendar

# def cal_disp(year, month):
#     if 1 <= month <= 12 and year > 0:
#         print(calendar.month(year, month))
#     else:
#         print("Invalid input! Please enter a valid month and year.")

# # Get user input
# yy = int(input("Enter YEAR: "))
# mm = int(input("Enter MONTH: "))

# # Call the function to display the calendar
# cal_disp(yy, mm)

#codedbyRMX