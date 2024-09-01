a=int(input("Enter size: "))
d1={}
for i in range(a):
    d2={}
    id=input("Enter id:")
    name = input("Enter name:")
    d2["name"]=name
    age=input("Enter age: ")
    d2["age"]=age
    salary=input("Enter salary: ")
    d2["salary"]=salary
    city=input("Enter city: ")
    d2["city"]=city
    d1[id]=d2
print(d1) 