s=input("Enter string: ")
char_count=input("Enter character: ")
count=0
for i in s:
    if i==char_count:
        count=count+1
if count>0:
    print(f"{char_count} appears {count} times in this string")
else:
    print(f"{char_count}  is not in this string")


