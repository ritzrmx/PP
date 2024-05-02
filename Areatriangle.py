def calculate_triangle_area(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Three sides of the triangle
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate and print the area
area = calculate_triangle_area(a, b, c)
print('The area of the triangle is %0.2f' % area)

