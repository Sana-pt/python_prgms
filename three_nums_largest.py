# a=int(input("Enter number1: "))
# b=int(input("Enter number2: "))
# c=int(input("Enter number3: "))
# if(a>b and a>c):
#     print(f"the given {a} is larger number")
# elif(b>a and b>c):
#     print(f"the given {b} is larger number")
# elif(c>a and c>b):
#     print(f"the given {c} is larger number")
# elif(a==b and b==c):
#     print(f"the given {a,b,c} are equal numbers")
# else:
#     print("Invalid number")



a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
c=int(input("Enter number3: "))
if(a>=b):
    if(a>=c):
        if(a==b==c):
            print("numbers are equal")
        else:
            print(f"the given {a} is larger number")
    else:
        print(f"the given {c} is larger number")
else:
    if(b>=c):
        print(f"the given {b} is larger number")
    else:
        print(f"the given {c} is larger number")

