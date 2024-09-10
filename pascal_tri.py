# n=4
# l1=[]
# for i in range(n):
#     l2=[]
#     for j in range(i+1):
#         if(j==0 or j==i):
#             l2.append(1)
#         else:
#             l2.append(l1[i-1][j-1]+l1[i-1][j])
#     l1.append(l2)
# print(l1)


n=4
ind=0
l=[]
for i in range(n):
    for j in range(n-i):
        print("  ",end="")
    for j in range(i+1):
        if(j==0 or j==i):
            l.append(1)
            print(l[ind],end="   ")
        else:
            l.append(l[ind-i-1]+l[ind-i])
            print(l[ind],end="   ")
        ind=ind+1
    print() 