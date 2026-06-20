def area(length, breadth):
    if length <= 0 or breadth <= 0:
        print("Length and Breadth must be greater than 0")
        return

    area = length * breadth

    print(f"Area of Rectangle = {area:.2f}")

area(5,3)