def string_times(str , n):
    result= str * n
    return result
    
    
def front_times(str, n):
  front_len = 3
  if len(str) < 3:
    return str * n
  front = str[:front_len]  
  return str[:(3 if len(str)>3 else len(str))]*n

def string_bits(str):
   return str[::2]

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  if b == c:
    return a
  if a == c:
    return b
  if a == b:
    return c  
  return a + b + c
    
    
def string_splosion(str):
  result= ''
  for i in range(1,len(str)+1):
    result = result + str[:i]
  return result


def cigar_party(cigars, is_weekend):
    if is_weekend and cigars >= 40:
        return True
    elif not is_weekend and cigars >= 40 and cigars <= 60:
        return True
    else:
        return False

def cigar_party2(cigars, is_weekend):
    if is_weekend:
        return (cigars >= 40)
    else:
        return (cigars >= 40 and cigars <= 60)


def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
     
  if speed <= 60:
      return 0
  if 60 < speed <= 80:
    return 1
  return 2


print(string_times('hello' , 4))
print(front_times('bestie', 4))
print(string_bits('everything'))
print(lone_sum(4, 2, 4))

