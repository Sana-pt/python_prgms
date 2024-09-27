class Stud:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    
    def display_s(self):
        print(f"Name:{self.name},Age{self.age},Grade:{self.grade}")

class Menu:
    def __init__(self):
        self.studs=[]

    def add_stud(self):
        name=input("Enter name: ")
        age=input("Enter age: ")
        grade=input("Enter grade: ")
        stud=Stud(name,age,grade)
        self.studs.append(stud)
        print("Added successful")
    
    def display_studs(self):
        if not self.studs:
            print("student not added")
        else:
            print("List: ")
            for stud in self.studs:
                stud.display_s()

    def choice(self):
        while True:
            print("\nMain Menu\n1.Add\n2.Display\n3.Exit")
            choice=input("Enter choice: ")
            if choice=='1':
                self.add_stud()
            elif choice=='2':
                self.display_studs()
            elif choice=='3':
                print("Exit")
                break
            else:
                print("Invalid choice")

menu=Menu()
menu.choice()


        
