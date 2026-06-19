def find_first_even(range_size):

    if range_size <= 0:
        print("Range size must be greater than 0")
        return

    for i in range(range_size):

        # Check even number
        if i % 2 == 0:
            print("First Even Number:", i)
            break

range_size = 10

find_first_even(range_size)