def login(user, pwd):

    if user != "":
        
        if pwd != "":
            
            if user == "admin" and pwd == "pass123":
                print("Login Successful")
            else:
                print("Invalid Credentials")

        else:
            print("Password Empty")

    else:
        print("Username Empty")

user = "admin"
pwd = "pass123"

login(user, pwd)