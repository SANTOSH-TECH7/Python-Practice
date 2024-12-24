s = "Santosh Ravi is a good man"
s = s.split()
update_words=[]
for word in s:
    if len(word)>1:
        update_word=word[0].upper()+word[1:-1]+word[-1].upper()
    else:
        update_word=word.upper()
    update_words.append(update_word)
result=" ".join(update_words)
print(result)