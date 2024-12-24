s="Naukrilearning@123"
alph=0
num=0
other=0
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n='1234567890'
for i in s:
    if i in lower or i in upper:
        alph+=1
    elif i in n:
        num+=1
    else:
        other+=1
print(alph,num,other)


s = "Naukrilearning@123"
alph = 0
num = 0
other = 0

# Loop through each character in the string
for i in s:
    if i.isalpha():  # Check if the character is an alphabet
        alph += 1
    elif i.isdigit():  # Check if the character is a digit
        num += 1
    else:  # If it's neither an alphabet nor a digit, count it as "other"
        other += 1

print(alph, num, other)
