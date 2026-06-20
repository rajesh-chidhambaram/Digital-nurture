def next_year_age():

    age = input("Enter Age: ")

    if age.isdigit():

        age = int(age)

        print("Next year you'll be", age + 1)

    else:
        print("Invalid Input")

next_year_age()