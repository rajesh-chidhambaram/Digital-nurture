import math

def calculate_area(radius):

    if radius <= 0:
        print("Radius must be greater than 0")
        return

    area = math.pi * radius ** 2


    print(f"Area of Circle = {area:.2f}")

radius = int(input("Enter the radius of the circle: "))

calculate_area(radius)