
l=int(input("Enter the limit: "))
sum=0
for i in range(l):
    n=int(input(f"Enter the number {i+1}: "))
    sum=sum+n
print("Sum of digits: ",sum)