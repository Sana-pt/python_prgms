# class Employee:
#     id=10
#     name="David"
#     def display(self):
#         print(self.id,self.name)
# a=Employee()
# a.display()

# class Employee:
#     id=10
#     name="David"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# a=Employee()
# a.display()

# class Employee:
#     id=10
#     name="David"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# del emp.id
# del emp.name
# emp.display()

# class Car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# c1=Car("Toyota",2016)
# c1.display()

# class Employee:
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp1=Employee("John",101)
# emp2=Employee("David",102)
# emp1.display()
# emp2.display()

# class Student:
#     def __init__(self):
#         print("this is non parametrized constructor")
#     def show(self,name):
#         print("Hello",name)
# student=Student()
# student.show("John")

# class Student:
#     def __init__(self,name):
#         print("this is parametrized constuctor")
#         self.name=name
#     def show(self):
#         print("Hello",self.name)
# student=Student("John")
# student.show()

# class Student:
#     roll_num=101
#     name="John"
#     def display(self):
#         print(self.roll_num,self.name)
# st=Student()
# st.display()

# class Student:
#     def __init__(self):
#         print("First constructor")
#     def __init__(self):
#         print("Second constructor")
# st=Student()

# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("John",101,22)
# print(getattr(s,'name'))
# setattr(s,"age",23)
# print(getattr(s,'age'))
# print(hasattr(s,'sid'))
# print(hasattr(s,'id'))
# delattr(s,'age')
# print(s.age)

# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.bark()
# d.speak()

# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
#     def speak(self):
#         print("dog speaking")
# d=Dog()
# d.bark()
# d.speak()

# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# class DodChild(Dog):
#     def eat(self):
#         print("Eating")
# d=DodChild()
# d.bark()
# d.speak()
# d.eat()


# class Calculation1:
#     def Sum(self,a,b):
#         return a+b
# class Calculation2:
#     def Mul(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def Div(self,a,b):
#         return a/b
# d=Derived()
# print(d.Sum(10,20))
# print(d.Mul(10,20))
# print(d.Div(10,20))


# class Parent:
#     def func1(self):
#         print("This function is in parent class")
# class Child1(Parent):
#     def func2(self):
#         print("this function is in child 1")
# class Child2(Parent):
#     def func3(self):
#         print("this function is in child 2")
# obj1=Child1()
# obj2=Child2()
# obj1.func1()
# obj1.func2()
# obj2.func1()
# obj2.func3()

