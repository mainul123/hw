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
