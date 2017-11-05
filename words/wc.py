def rp(w):
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
    f = open(f).read()
    l=[]
    for w in f.split():
        w = w.lower()
        w = rp(w)
        l.append(w)
    d = bwcd(l)
    return d


d = bwcff("hamlet.txt")
