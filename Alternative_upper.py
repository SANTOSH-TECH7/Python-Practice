s="Santosh Ravi is a good man"
s_new=""
for i in range(0,len(s)):
    if i%2!=0:
        s_new=s_new + s[i].upper()
    else:
        s_new=s_new + s[i].lower()
print(s_new)
    
    