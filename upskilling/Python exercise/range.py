def print_numbers(count):

    if count <= 0:
        print("Loop count must be greater than 0")
        return


    for i in range(count):
        print(i + 1)


count = 5

print_numbers(count)