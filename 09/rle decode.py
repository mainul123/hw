def rle(s):
    encoded = []
    while len(s)>1:
        runlen = 1
        runchar = s[0]
        while runlen < len(s) and s[runlen]==runchar:
            runlen = runlen + 1
        if runlen>1:
            encoded.append(runlen)
        encoded.append(runchar)
        s=s[runlen:]
    return encoded


s = "aavbbbbbccdddddd"
print(s)
print(rle(s))

def rle_decode(s):
	decode = ''
	x = 0
	while x < len(s):

		if (isinstance(s[x],int) == True):
			decode = decode + (s[x+1]*s[x])
			x = x + 2
		else:
		  decode = decode + (s[x])
		  x = x + 1
	return decode

print([2,'a', 3, 'b', 'c', 2,'d'])
print(rle_decode([2,'a', 3, 'b', 'c', 2,'d']))