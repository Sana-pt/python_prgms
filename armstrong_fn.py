def armstrong(a):
    l=len(a)
    sum=0
    for i in a:
        n=int(i)
        sum=sum+(n**l)
    if a==str(sum):
        print("Armstong")
    else:
        print("Not armstrong")

num=input("Enter a num: ")
armstrong(num)
    
