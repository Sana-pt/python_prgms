a=int(input("Enter no.of elements in a list: "))
e=[]
for i in range(a):
    n=int(input(f"Enter the num {i+1}: "))
    e.append(n)
print(e)
d1={}
for num in e:
    if num in d1:
        d1[num]=d1[num]+1
    else:
        d1[num]=1
print("ELements: ",d1)
largest_num=n

    

