
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    print("1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Exit")
    choice=int(input("Enter a choice: "))
    if choice==1:
        a=int(input("Enter a num1: "))
        b=int(input("Enter a num2: "))
        print("sum is: ",add(a,b))
    elif choice==2:
        a=int(input("Enter a num1: "))
        b=int(input("Enter a num2: "))
        print("diff is: ",sub(a,b))
    elif choice==3:
        a=int(input("Enter a num1: "))
        b=int(input("Enter a num2: "))
        print("prod is: ",mul(a,b))
    elif choice==4:
        a=int(input("Enter a num1: "))
        b=int(input("Enter a num2: "))
        if b==0:
            print("zero can't be divided.")
        else:
            print("quot is: ",div(a,b))
    else: 
        print("exit")
        break

    
    

   

