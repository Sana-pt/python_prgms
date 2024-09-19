a=int(input("Enter limit: "))
odd_even={}
odd_even={str(i):str(i+1) for i in range(1,a) if i%2!=0}
odd=''.join([str(i) for i in range(1,a) if i%2!=0])
even=''.join([str(i) for i in range(2,a+1) if i%2==0])
odd_even={odd:even}
print(odd_even)