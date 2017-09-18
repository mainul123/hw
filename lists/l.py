l=[]
l2=['a','b','c','d','e','f','g']

print(len(l2))
print(l2[2])

l3 = l2[2:5]
print(l3)

s="abcdefg"
print(s[2])
print(s[2:5])

l.append(2)
l.append(4)
print(l)

s="everybody has a plan until they get punched in the mouth"
slist = s.split()
for word in slist:
    print(word)
    

l.append(l2)
l3=['a','b','c']
l4= [1,2,3,4,5]
longlist = l3+l4