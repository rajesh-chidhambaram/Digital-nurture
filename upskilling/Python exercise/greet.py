def greet():

    name = input("Enter Name: ")

    if name.strip() == "":
        print("Name cannot be empty")
    else:
        print(f"Hello {name}")

greet()