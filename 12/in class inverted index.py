import csv

def build_inverted_index(filename):
    csv_reader =csv.reader(open(filename))
    for line in csv_reader:
        key = line[0]
        textstring = line[1]
        print(textstring)
        cleantext = ""
        for letter in textstring:
            if letter.isalpha():
                cleantext = cleantext + letter
            else:
                cleantext = cleantext + " "
        worlist  = cleanlist.split()
        for word in wordlist:
            d.setdefault(word.[])
            d[word].append(document)
        return d
sample_index = []
        
        
    build_inverted_index("sample-text",0,1)