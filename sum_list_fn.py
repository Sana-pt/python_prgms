def sum_list():
    a=input("Enter list of nums in commas: ")
    list=[int(n) for n in a.split(',')]
    sum=0
    for n in list:
        sum=sum+n
    return sum
r=sum_list()
print("sum of list: ",r)