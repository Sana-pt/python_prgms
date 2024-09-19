def l(n):
    length=0
    while(n!=0):
        length=length+1
        n=n//10
    return length
num=int(input("Enter a number: "))
rem=0
sum=0
len=l(num)
n=num
while(num>0):
    rem=num%10
    sum=sum+int(pow(rem,len))
    num=num//10
    len=len-1
if sum==n:
    print("disarium")
else:
    print("not disarium")