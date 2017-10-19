def freq(n,l):
    start = 0
    for num in l:
        if (n == num):
            start += 1
    return start


def min(l):
    ans = l[0]
    for i in range(1,len(l)):
        if l[i] < ans:
            ans = l[i]
    return ans


def mode(l):
    mode_in_l = 0
    current_mode = 0
    for int in l:
        if freq(int,l) > mode_in_l:
            mode_in_l = int
            current_mode = freq(int,l)
    return mode_in_l

s = [1,3,3,3,7,6,543,534,534,5,343,3,]

print(mode(s))


  