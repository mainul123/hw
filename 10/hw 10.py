def remove_non_alpha(w):
    """
    input: w - string representing a "word"
    output: the string with non alpha chars removed
    """
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def bwcd(wordlist):
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
        
    return d

def bwcff(f):
    """
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
             of the number of times each word occursb
    """
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = remove_non_alpha(w)
        l.append(w)
    d = bwcd(l)
    return d



def add_words(f):
    text = open(f).read()
    words_dict = {}
    words_list = []
    for word in text.split():
        word = word.lower()
        word = remove_non_alpha(word)
        words_list.append(word)
    for i in range(len(words_list)):
        word = words_list[i]
        next_word = words_list[i+1]
        if word in words_dict:
            words_dict[word].append(next_word)
        elif word not in words_dict:
            words_dict[word] = [next_word]
        return words_dict
    
print(add_words("hamlet.txt"))
            
        
        
        
    
    

#d = bwcff("hamlet.txt")
#print(bwcff("hamlet.txt"))
