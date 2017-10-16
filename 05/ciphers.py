

#letter shift
for letter in input():
    ascii_val = ord(letter)
    plus = ascii_val + 1
    newchar = chr(plus)
    print(letter, ":", ascii_val, " rotated:", newchar, ":", plus)
    
    
    
    #string shift
message = "just a simple test!"
key = 8
coded_message = ""
for ch in message:
    code_val  = ord(ch) + key
    if ch.isalpha():
        if code_val > ord('z'):          
            coded_message = coded_message + chr(code_val)
    else:
        coded_message = coded_message + ch
print (message)
print (coded_message)

    #all possible combos for string

from itertools import permutations
perms = [''.join(p) for p in permutations('stack')]
perms


