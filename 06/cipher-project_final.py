import math
real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,
              0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,
              0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]



def rotate_letter(c , r):
    letter_value = ord(c) + r
    if letter_value > 122:
        letter_value = letter_value - 26
    return chr(letter_value)


def encode_string(str, r):
    s = str.lower()
    encoded_string = ''
    for i in s:
        if  ord(i) >= 97 and ord(i) <= 122: 
            encoded_string += rotate_letter(i, r)     
        else:
            encoded_string += i
    return encoded_string



#shift through the alphabet & encodes the string for each possible shift
def full_encode(s):
    entire_string = ''
    for i in range (26):
        entire_string += encode_string(s, i) + '\n'
    return entire_string

print(rotate_letter('c',5))
print(encode_string('hello everyone', 4))
print(full_encode('hello world!'))




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

def print_vector_table(v):
    s="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i]," : ",v[i])


def decode(s):
    rotations = []
    frequencies = []
    distances = []
    for i in range(26):
        rstring = encode_string(s,i)
        freq = build_frequency_vector(rstring)
        rotations.append(rstring)
        frequencies.append(freq)
        d = distance(freq, real_stats)
        distances.append(d)
    # find the smallest value and its index
    min_index = 0
    min_value = distances[0]
    for i in range(1,len(distances)):
        if distances[i] < min_value:
            min_value = distances[i]
            min_index = i
    print(min_index, min_value)
    return(encode_string(s,min_index))
    
    
s2 = "this is a longer sentence with more letters so hopefully it will be closer to the real distribution"

encoded = encode_string(s2,5)
decoded = decode(encoded)
print("Original: ",s2)
print("Encoded: ", encoded)
print("Decoded: ", decoded)