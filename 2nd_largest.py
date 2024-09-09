n=int(input("Enter a the size of the list:"))
a=[]
print("Items in the List")
for i in range(n):
    item=int(input())
    a.append(item)

print("The List:",a)
if a[0]>a[1]:
    largest=a[0]
    second_largest=a[1]
else:
    largest=a[1]
    second_largest=a[0]
for i in range(2,n):
    if a[i]>largest:
        second_largest=largest
        largest=a[i]
    elif a[i]>second_largest and a[i]!=largest:
        second_largest=a[i]
print("second largest: ",second_largest)