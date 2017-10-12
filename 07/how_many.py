def freq(n,l):
    l = [2,3,4,5,6,7,7,7,7,7,7,4,7,6,4,4,2,11,3,43]
    n = len([i for i in l if i == 7])
    return n

#change l value to find exact value

def min(l):
    l = [2,3,4,5,6,7,7,7,7,7,7,4,7,6,4,4,2,11,3,43]
    x=l[0]
    for i in l:
        if i < x:
            x=i
    print(x)

from statistics import mode
l = [2,3,4,5,6,7,7,7,7,7,7,4,7,6,4,4,2,11,3,43]
mode(l)   

  