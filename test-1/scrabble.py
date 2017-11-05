rawvals = {
    "aeioulnrst"  : 1,
    "dg"          : 2,
    "bcmp"        : 3,
    "fhvwy"       : 4,
    "k"           : 5,
    "jx"          : 8,
    "qz"          : 10 
}


scores = {}
for k in rawvals:
    for letter in k:
        scores[letter] = rawvals[k]



def calc_score(word):
    score = 0
    for letter in word:
        score = score + scores[letter]
    return score

