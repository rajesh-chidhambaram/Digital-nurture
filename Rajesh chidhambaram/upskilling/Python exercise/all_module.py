from math import *

def math_demo(number):

    if number < 0:
        print("Number cannot be negative")
        return

    square_root = sqrt(number)

    square = pow(number, 2)

    pi_value = pi

    print(f"Number      : {number}")
    print(f"Square Root : {square_root:.2f}")
    print(f"Square      : {square:.2f}")
    print(f"Pi Value    : {pi_value:.5f}")


number = int(input("Enter a number: "))

math_demo(number)