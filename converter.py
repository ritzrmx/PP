def km_to_ml(km):
    miles = km * 0.621371
    return miles

def c_to_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

while True:
    print("\nMenu:")
    print("1. Convert Kilometers to Miles")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        miles = km_to_ml(km)
        print(f"{km} km is equal to {miles} miles.")

    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = c_to_f(celsius)
        print(f"{celsius} °C is equal to {fahrenheit} °F.")

    elif choice == '3':
        exit()

    else:
        print("!! Invalid choice !!")
        
        
        
        
        
        
        
        
        #codedbyRMX
