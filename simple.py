u={"username":"1234"}
users={}
person=[]
def main():
    while True:
        print(" Main Menu\n1.register\n2.Login\n3.Exit")
        choice=int(input("Enter choice: "))
        if choice==1:
            register()
        elif choice==2:
            login()
        elif choice==3:
            print("Exit")
            break
        else:
            print("Invalid choice")
def register():
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username=="username" and password=="1234":
        while True:
            print("1.Add person\n2.Dispaly person\n3.Exit")
            choice=int(input("Enter choice: "))
            if choice==1:
                    add()
            elif choice==2:
                    display()
            elif choice==3:
                print("Exit")
                break
            else:
                print("Invalid")
    else: 
         print("Invaild username")
def add():
    name=input("Enter name: ")
    age=input("Enter age: ")
    address=input("Enter address: ")
    person.append({"name":name,"age":age,"address":address})
    print("person added")
def display():
    if person:
        for name,i in person():
            print(f"name: {name}")
            print(f"age: {['age']}")
            print(f"address: {['address']}")
    else:
        print("no person")

def login():
    username=input("Enter username: ")
    password=input("Enter password: ")
    if['username']==username and ['password']==password:
        print("done")
    else:
        print("Invalid")
u={"username":"1234"}
users={}
person=[]
def main():
    while True:
        print(" Main Menu\n1.register\n2.Login\n3.Exit")
        choice=int(input("Enter choice: "))
        if choice==1:
            register()
        elif choice==2:
            login()
        elif choice==3:
            print("Exit")
            break
        else:
            print("Invalid choice")
def register():
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username=="username" and password=="1234":
        while True:
            print("1.Add person\n2.Dispaly person\n3.Exit")
            choice=int(input("Enter choice: "))
            if choice==1:
                    add()
            elif choice==2:
                    display()
            elif choice==3:
                print("Exit")
                break
            else:
                print("Invalid")
    else: 
         print("Invaild username")
def add():
    name=input("Enter name: ")
    age=input("Enter age: ")
    address=input("Enter address: ")
    person.append({"name":name,"age":age,"address":address})
    print("person added")
def display():
    if person:
        for name,i in person.items():
            print(f"name: {name}")
            print(f"age: {i['age']}")
            print(f"address: {i['address']}")
    else:
        print("no person")

def login():
    username=input("Enter username: ")
    password=input("Enter password: ")
    if['username']==username and ['password']==password:
        print("done")
    else:
        print("Invalid")
main()