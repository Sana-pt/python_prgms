print("1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division")
c=int(input("Enter your choice: "))
a=int(input("Enter num1: "))
b=int(input("Enter num2: "))

if(c==1):
    print("answer: ",a+b)
  
elif(c==2):
    print("answer: ",a-b)
   
elif(c==3):
    print("answer: ",a*b)
    
elif(c==4):
    print("answer: ",a/b)
    
else:
    exit 
