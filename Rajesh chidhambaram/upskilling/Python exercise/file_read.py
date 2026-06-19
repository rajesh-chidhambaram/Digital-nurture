def read_file():
    try:
        file = open("greeting.txt", "r")
        content = file.read()
        print("Content of 'greeting.txt':")
        print(content)
    except FileNotFoundError:
        print("File 'greeting.txt' not found. Please create it first using file_write.py.")
    finally:
        try:
            file.close()
        except NameError:
            pass
read_file()