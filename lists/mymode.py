import random

def f(l):
    for i in l:
        pass

    for i in l:
        pass

    
def freq(n, l):
    count = 0
    for i in l:
        if i == n:
            count += 1
    return count

#finds minimum value in list
def min(l):
    min = l[0]

    for i in l:
        if i < min:
            min = i
    return min
def mode1(l):
    mode_so_far = freq(l[0],l)
    mode_index = 0
    for index,value in enumerate(l):
        next_freq = freq(value,l)
        if (next_freq > mode_so_far):
           mode_so_far = next_freq
           mode_index = index
    return l[mode_index]

def mode2(l):
    buckets = []
    for i in range(100):
        buckets.append(0)

    for item in l:
        buckets[item]=buckets[item]+1

    max_index=0
    for index,item in enumerate(buckets):
        if buckets[index] > buckets[max_index]:
            max_index = index
    return max_index

def build_random_list(items):
    l = []
    for i in range(items):
        l.append(random.randrange(10))
    return l

l = [1,3,7,1,6,1,7,4,7,7,7,7,7,7]

print(mode1(l))
print(mode2(l))
