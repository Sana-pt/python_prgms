

class Display:
    def display(self):
        return f"Name:{self.name},age:{self.age}"

class Details:
    def details(self):
        students=[]
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        c=Display()
        c.name=name
        c.age=age
        students.append(c)

        for c in students:
            print(c.display())


f=Details()
f.details()