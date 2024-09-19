def rev(s):
    r=list(s)
    a,b=0,len(s)-1
    v='aeiouAEIOU'
    while a<b:
        while a<b and r[a] not in v:
            a=a+1
        while a<b and r[b] not in v:
            b=b-1
        r[a],r[b]=r[b],r[a]
        a=a+1
        b=b-1
    rev_str=''
    for i in r:
        rev_str=rev_str+i
    return rev_str
s=input("Enter string: ")
print("Reversed: ",rev(s))