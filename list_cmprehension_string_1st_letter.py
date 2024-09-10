a=int(input("Enter size of list: "))
l=[]
for i in range(a):
    b=input("Enter strings: ")
    l.append(b)
print(l)
l1=[i[0] for i in l]
print(l1)




