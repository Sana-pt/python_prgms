u=[]

def main():
    while True:
        print("main menu\n1.Register\n2.login\n3.Exit")
        choice=int(input("Enter choice: "))
        if choice==1:
            register()
        elif choice==2:
            login()
        elif choice==3:
            print("Exit")
            break
        else:
            print("invalid choice")
def register():
    name=input("enter name: ")
    age=input("enter age: ")
    adress=input("enter address: ")
    phone_num=input("enter phone_num: ")
    username=input("enter username: ")
    password=input("enter password: ")
    
    u.append({"username":username,"password":password})
    print("Done")
    
def login():
    username=input("enter username: ")
    password=input("enter password: ")
    for user in u:
        if user["username"]==username and user["password"]==password:
            print("done") 
        else:
            print("invalid")
main()

    