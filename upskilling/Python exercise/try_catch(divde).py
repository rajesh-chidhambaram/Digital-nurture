def divide_numbers(num1, num2):

    try:

        result = num1 / num2

        print("Result =", result)

    except ZeroDivisionError:

        print("Error: Cannot divide by zero")

divide_numbers(10, 2)