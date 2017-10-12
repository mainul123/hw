
import math
f = open("sher.dat").read()
for line in f:
    f.join(e for e in f if e.isalnum()) #removes all charachters that arent a letter and joins them together
    print(f.lower())

freqs = []
for line in 'sher.dat':
    for char in line:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

print (freqs)


def rotate_char(c,r):
    """
    Rotates character c by amount r. Wraps if past z****
    """
    v = ord(c)
    v = v - 97 # shift down so that 'a' is 0
    v = (v + r)%26
    v = v + 97 # shift back up so that 'a' is 97
    result = chr(v)
    return result

def encode_string(s,r):
    """
    rotate a string (lower case letters only)
    """
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter = rotate_char(letter,r)
        result = result + letter
    return result

r = encode_string("The quick brown fox jumps over a lazy dog",4)
print(r)


def distance(l1,l2):
    length = len(l1)
    if length>len(l2):
        length = len(l2)
    sum=0
    for i in range(length):
        sum = sum + (l1[i]-l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d



def build_frequency_vector(s):
    # count the letters in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)
    return v
#f = build_frequency_vector("they ate my pie")
#print(f)


def append_vectors(s):
   vlist=[]
   for i in range(26):
        s2= encode_string(s,i)
        v= build_frequency_vector(s2)
        vlist.append(v)
   return vlist
        
freqs = append_vectors('The quick brown fox jumps over a lazy dog')
print(freqs)



def print_vector_table(v):
    s="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i]," : ",v[i])


def decode(s):
    rotations = []
    frequencies = []
    for i in range(26):
        rstring = encode_string(s,i)
        freq = build_frequency_vector(rstring)
        rotations.append(rstring)
        frequencies.append(freq)
        d= distance(freq.freqs)
        distances.append(d)
    #ffind the smalled value and its index)
    min_index = 0
    min_value = distances[0]
    for i in range(1,len(distances)):
        if distances[i] < mind_value:
            min_value = distances[i]
            min_index = i
    print(min_index, min_value)
    
    
s= 'this is a longer sentence with more letters so hopefully it will be closer to the real distribution'    
    
encoded = encode_string(s,1)
decode(encoded)
    
    
    
    
