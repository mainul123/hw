#Mainul  and Oliver's MADLIDcode


print('check out our newbie madlib code')

nouns = ['boy', 'girl', 'gorilla', 'apple', 'sandwich']
verbs = ['eat', 'sleep', 'dance', 'swim']
adjective= ['stupid','grey', 'black']
story = 'Everyone knows that I VERB goes with NOUN ADJECTIVE.'
import random 

if 'VERB'in story:
    random.shuffle(verbs)
    num = story.find('VERB')
    story = story[:num] + verbs[2] + story[num+4:]
    
if 'NOUN'in story:
    random.shuffle(nouns)
    num = story.find('NOUN')
    story = story[:num] + nouns[1] + story[num+4:]

if 'ADJECTIVE.'in story:
    random.shuffle(adjective)
    num = story.find('ADJECTIVE')
    story = story[:num] + adjective[1] + story[num+9:]


print(story)