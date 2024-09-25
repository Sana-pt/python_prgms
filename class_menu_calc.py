class Calculator:
    def add(self,a,b):
       print(f"sum of {a}+{b}=",a+b)

    def sub(self,a,b):
       print(f"difference of {a}-{b}=",a-b)
     

    def mul(self,a,b):
       print(f"product of {a}*{b}=",a*b)
    
    def div(self,a,b):
        if b==0:
           print("No divisiion by zero")
        else:
           print(f"quotient of {a}/{b}=",a/b)

    def menu(self):
       while True:
          print("\nMenu driven\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
          choice=int(input("Enter choice: "))
          if choice==5:
             print("Exit")
             break
          elif choice in [1,2,3,4]:
             try:
                a=int(input("Enter 1st number: "))
                b=int(input("Enter 2st number: "))
                if choice==1:
                   self.add(a,b)
                elif choice==2:
                   self.sub(a,b)
                elif choice==3:
                   self.mul(a,b)
                elif choice==4:
                   self.div(a,b)
             except ValueError:
                print("Invalid")
          else:
            print("Invalid choice")
calc=Calculator()
calc.menu()
              
               


