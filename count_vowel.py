def count_vowels(s):
    count=0
    for i in range(length):
        if s[i] in "AEIOUaeiou":
            count+=1
    return (count)
s=input("Enter the sentence: ")
length=len(s)
print("Count: ",count_vowels(s))
