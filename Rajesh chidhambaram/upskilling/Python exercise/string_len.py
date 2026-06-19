def string_length(s):
    if not isinstance(s, str):
        print("Input must be a string")
        return

    length = len(s)
    print(f"Length of the string '{s}' is {length}")

text = input("Enter a string: ")
string_length(text)

