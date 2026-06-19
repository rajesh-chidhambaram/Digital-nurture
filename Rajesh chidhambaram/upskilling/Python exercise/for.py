def print_numbers(count):

    if count <= 0:
        print("Invalid Count")
        return

    for i in range(count):
        print(i + 1)

print_numbers(5)