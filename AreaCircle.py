import math
def area_of_circle(radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle : "))

result  = area_of_circle(radius)

print(f"The area of the circle with radius {radius} is : {result}")
