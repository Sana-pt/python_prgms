n=5
for i in range(n+1):
    for j in range(n-i):
        print("",end=" ")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()