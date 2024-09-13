d1={}
while True:
    print("   MENU DRIVEN\n1.Register\n2.Login\n3.Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
            username=input(f"Enter username: ")
            if username in d1:
                print("Username exist.Select another username ")
            else:
                password=input(f"Enter password : ")
                if not username or not password:
                    print("username and password are empty")
                else:
                    d1[username]={"username":username,"password":password}
                    print("Successfully registered")
    elif choice==2:
        username=input("Enter username: ")
        password=input("Enter password: ")
        if username in d1 and d1[username]["password"]==password:
            print("Successfully login")
        else :
            if username not in d1:
                print("Invalid username")
            elif d1[username]["password"] != password:
                print("Invalid password")
            new_username=input("Enter new usename: ")
            if new_username in d1:
                print("Username exists.Enter another username")
            else:
                new_password=input("Enter new password: ")
                if not new_username or not new_password:
                    print("username and password are empty")
                else:
                    d1[new_username]={"username":new_username,"password":new_password}
                    print("successfully registered new user")
                
            
    elif choice==3:
        print("Exit")
        break
    else:
         print("invalid")







