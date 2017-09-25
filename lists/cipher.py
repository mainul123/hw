l='a'
print(l,ascii_val)

for letter in "abcdefg":
    ascii_val = ord(letter)
    plus = ascii_val + 3
    newchar = chr(plus)
    print(letter,":",ascii_val," rotated: ",newchar,':',plus)

