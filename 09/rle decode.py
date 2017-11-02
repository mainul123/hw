
def rle_decode(s):
	decode = ''
	x = 0
	while x < len(s):

		if (isinstance(s[x],int) == True): #isinstance checks to see the type, therefore an integer
			decode = decode + (s[x+1]*s[x])
			x = x + 2
		else:
		  decode = decode + (s[x])
		  x = x + 1
	return decode

print([2,'a', 3, 'b', 'c', 2,'d'])
print(rle_decode([2,'a', 3, 'b', 'c', 2,'d']))