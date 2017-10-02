

def rotate_char(c,r):
    """
    Rotates character c by amount r. Wraps if past z
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

r = encode_string("abde",3)
print(r)
