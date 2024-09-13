d1=[]
while True:
    print("1.Registeration\n 2.Display\n 3.Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
         a=int(input("Enter no.of person for register: "))
         for i in range(a):
              d2=[]
              id=int(input(f"Enter id of person {i+1}:"))
              name=input(f"Enter name of person {i+1}: ")
              d2.append(name)
              age=int(input(f"Enter age of person {i+1}: "))
              d2.append(age)
              city=input(f"Enter city of person {i+1}: ")
              d2.append(city)
              d1.append(d2)
              print("Successfully registered")
    elif choice==2:
          if d1:
               name=input("Enter name of a person to display: ")
               for person in d1 :
                    if person[0]==name:
                         print(person[1])
                         print(person[2])
                         break
               else:
                    print("No person")
          else:
               print("No registered person")
    elif choice==3:
         print("Exit")
         break
    else:
         print("invalid")





