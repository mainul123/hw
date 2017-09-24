import random

def comma_code(subject):

     a = (len(list(subject)) - 1)

     for i in range(0, len(list(subject))):

          if i != a:
               print(str(subject[i]) + ', ', end="")

          else:
              print('and '+ str(subject[i]))            


spam = ['apples','banana','tofu','cats']