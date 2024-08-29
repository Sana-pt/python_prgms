year=int(input("Enter year: "))
if(year%4==0 and year%100!=0):
    print(f"the {year} is a leap year")
elif(year%100==0):
    print(f"the {year} is not a leap year")
elif(year%400==0):
    print(f"the {year} is a leap year") 
else:
    print(f"the {year} is not a leap year")