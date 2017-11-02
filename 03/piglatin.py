
pyg ="ay"

original = input('Enter a Word:')

if len(original) > 0 and original.isalpha():
    print(original)
    word = original.lower()
    first = original[0]
else:
    print ("empty")

new_word = word + first +pyg
new_word = new_word[1:]
print (new_word)


'''
notes for me**

first new_word line doesnt remove the first letter

.isalpha= must be a letter

second new word runs it from the second word and
ends at the last word 

'''

