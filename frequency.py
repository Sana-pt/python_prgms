a=int(input("Enter limits: "))
l=[]
for i in range(a):
    n=int(input(f"Enter num {i+1}: "))
    l.append(n)
print(l)
d1={}
for num in l:
    if num in d1:
        d1[num]+=1
    else:
        d1[num]=1
print(d1)
