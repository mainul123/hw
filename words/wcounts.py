def remove_puncuation(w):
    result=""
    for letter in w:
        if letter.isalpha():
            result = result + letter
    return result

def build_word_count_dict(wordlist):
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
    return d

def build_word_count_from_file(fname):
    f = open(fname).read()
    l=[]
    for w in f.split():
        w = w.lower()
        w = remove_puncuation(w)
        l.append(w)
    d = build_word_count_dict(l)
    return d

d=build_word_count_from_file('hamlet.txt')

