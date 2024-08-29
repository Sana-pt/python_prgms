grade=int(input("Enter your mark: "))
if(grade>100):
    print(f"{grade} is invalid")
elif(grade>=90):
    print("A+")
elif(grade>=80):
    print("A")
elif(grade>=70):
    print("B+")
elif(grade>=60):
    print("B")
elif(grade>=50):
    print("C+")
elif(grade>=40):
    print("C")
else:
    print("Fail")

