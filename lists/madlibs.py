import random

src="one day NOUN VERB NOUN"

def get_word(l):
    nouns=['bob','godzilla','ape','narwhal']
    return random.choice(l)
 
def get_verb():
    verbs=['ate','ran','bludgeoned','swam']
    return get_word(verbs)


def get_noun():
    return get_word(nouns)

def mad_lib_fill(sentence):
    slist = sentence.split()
    rlist=[]
    for word in slist:
        if word=='NOUN':
            nword = get_noun()
        elif word=="VERB":
            nword = get_verb()
        else:
            nword = word
        rlist.append(nword)
    return " ".join(rlist)
new_sentence = mad_lib_fill(src)
print(new_sentence)
