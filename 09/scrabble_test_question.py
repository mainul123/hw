def score(w):
  POINTBOARD={
      1:'AEIOULNRST',
      2:'DG',
      3:'BCMP',
      4:'FHVWY',
      5:'K',
      8:'JX',
      10:'QZ'  }
  
  
  sum=0
  w = w.upper()
  for characters in w:
    for points in POINTBOARD.keys():
        if characters in POINTBOARD[points]:
            sum=sum+points
  return w, sum

print(score('EVERYTHING'))
