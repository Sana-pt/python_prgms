num=int(input("Enter a number: "))
factorial=1
if(num==0):
    print(f"The facctorial of 0 is 1")
elif(num>0):
    for i in range(1,num+1):
         factorial*=i
    print(f"The factorial of {num} is {factorial}")
else:
    print("No factorial")
