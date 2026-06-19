def countdown(count):

    if count <= 0:
        print("Count must be greater than 0")
        return

    while count > 0:
        print(count)
        count -= 1

count = 5

countdown(count)