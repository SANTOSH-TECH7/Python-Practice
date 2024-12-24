str1="listen"
str2="silent"
str1=str1.replace(" ","").lower()
str2=str2.replace(" ","").lower()

if sorted(str1)==sorted(str2):
    print("it is anagram")
else:
    print("it is not anagram")