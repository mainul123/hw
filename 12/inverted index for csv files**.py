import csv

def reader(a):
    mydict = {}
    for row in a:
        row[1] = row[1].split()
        for word in row[1]:
            mydict[word] = []
        for k, v in mydict.items():
            for word in row[1]:
                if k == word:
                    v = v.append(row[8])
    return mydict

def wordfinder(word, dict):
    criminals=[]
    for k, v in dict.items():
        if word in v[0]:
            criminals.append(k)
    return criminals

a={}
with open('offenders-clean.csv') as csvfile:
        readstuff = csv.reader(csvfile)
        a=(reader(readstuff))

b=wordfinder("death", a)
print(b) 


