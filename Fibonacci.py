def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    return fib_series

try:
    user_input = int(input("Enter number for Fibonacci series: "))
    if user_input <= 0:
        print("Enter Positive number")
    else:
        result = fibonacci(user_input)
        print(f"The Fibonacci series with {user_input} terms is: {result}")
except ValueError:
    print("!! Invalid input !!")
