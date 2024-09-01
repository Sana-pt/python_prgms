a=int(input("Enter how many numbers: "))
numbers=[]
even_count=0
odd_count=0
for i in range(a):
        num=int(input(f"Enter number{i+1}: "))
        numbers.append(num)
for num in numbers:
        if num%2==0:
                even_count+=1
                
        else:
                odd_count+=1
                
print(f"odd numbers count:{even_count}")
print(f"even numbers count:{odd_count}")