a=int(input("Enter no.of students: "))
d1=[]
for i in range(a):
    d2={}
    ID=input("Enter ID: ")
    d2["ID"]=ID
    name=input("Enter name: ")
    d2["name"]=name
    age=input("Enter age: ")
    d2["age"]=age
    
    marks=[]
    for j in range(0,3):
        mark = int(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)
    d2["marks"]=marks
    d1.append(d2)
print(d1)




    

