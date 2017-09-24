#Mainul  and Oliver's MADLIDcode


print('check out newbie madlib code')

nouns = ['boy', 'girl', 'gorilla', 'apple', 'sandwich']
verbs = ['eat', 'sleep', 'dance', 'swim']
adjective= ['stupid']
story= ['Every', 'day', 'I', 'VERB', 'to', 'school', 'and', 'hope', 'that', 'I', 'can', 'bring', 'a', 'NOUN', 'with', 'me', 'This', 'makes', 'me', 'feel', 'ADJECTIVE.']

import random 

if 'VERB'in story:
 loc = story.index('VERB')
story.remove('VERB')
story.insert(3, random.choice(verbs))

if 'NOUN'in story:
 loc = story.index('NOUN')
story.remove('NOUN')
story.insert(13, random.choice(nouns))

if 'ADJECTIVE.'in story:
 loc = story.index('ADJECTIVE.')
story.remove('ADJECTIVE.')
story.insert(20, random.choice(adjective))



print(story)