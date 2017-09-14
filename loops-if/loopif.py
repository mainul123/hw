
def strexp_while(s):
    '''
    if s = abc then return aababc
    '''
    l = len(s)
    result = ""
    i = 0
    while i < l:
        part = s[0:i+1]
        result = result + part
        i=i+1
    return result
    

def strexp_for(s):
    '''
    if s = abc then return aababc
    '''
    l = len(s)
    result = ""
    for i in range(l):
        part = s[0:i+1]
        result = result + part
    return result

def strbits(s):
    l = len(s)
    result=""
    for i in range(l):
        if i%2==0:
            result = result + s[i]
    return result

print(strexp_while("abcd"))
print(strexp_for("abcd"))
print(strbits("abcdefg"))
