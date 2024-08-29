height=float(input("Enter height: "))
weight=float(input("Enter weight: "))
bmi=weight/float(height*height)
if(bmi<18.5):
    print(f"the {bmi:.2f} is underweight")
elif(18.5<=bmi<24.9):
    print(f"the {bmi:.2f} is normal weight")
elif(25<=bmi<29.9):
    print(f"the {bmi:.2f} is over weight")  
else:
    print(f"the {bmi:.2f} is obese")