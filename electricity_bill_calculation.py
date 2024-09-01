units=int(input("Enter units: "))
if(units<=100):
    print(f"{units*5} units")
elif(units<=200):
    print(f"{100*5+(units-100)*10} units")
elif(units>=200):
    print(f"{100*5+100*10+(units-200)*15} units")
else:
    print("invalid")



