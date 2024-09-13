a=int(input("Enter size of list: "))
l=[]
for i in range(a):
    b=input(f"Enter strings {i+1}: ")
    l.append(b)
print(l)
d1={fruit:len(fruit) for fruit in l}
print(d1 )



