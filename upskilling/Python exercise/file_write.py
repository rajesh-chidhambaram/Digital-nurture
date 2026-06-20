def file_write():
    file = open("greeting.txt","w")

    file.write("Hello World!\n")

    file.close()

    print("File 'greeting.txt' has been created and written successfully.")

file_write()