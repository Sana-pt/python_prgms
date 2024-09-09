a=int(input("Enter limits: "))
l=[]
for i in range(a):
    n=int(input("Enter num: "))
    l.append(n)
print(l)
d1={}
for num in l:
    if num in d1:
        d1[num]+=1
    else:
        d1[num]=1
print(d1)
duplicates=[]
counts=[]
for num,count in d1.items():
    if count==1:
        duplicates.append(num)
        counts.append(count)
print("Duplicates: ",duplicates)
print("Counts: ",counts)
print(max(duplicates))






    
    
    
