import random

def comma_code(q):
    str= ''
    for i in q:
        if i == q[-1]:
            str += 'and ' + i
        else:
            str += i + ', '
    return str  

spam = ['apples','banana','tofu','cats']

print(comma_code(spam))



