a=int(input("Enter how many elements: "))
n=[]
for i in range(5):
    num=int(input(f"Enter number{i+1}: "))
    n.append(num)
sum=0
for num in n:
    sum+=num
print("sum of all: ",sum)
