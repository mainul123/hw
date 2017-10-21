




def are_happy(s):
    '''
    This might miss some of the real edge cases in the hackerrank
    problem. I haven't read the problem carefully in over a year and 
    forget what it specified for things like lists of only spaces,
    lists with only one bug etc.

    Also, the Hackerrank question uses an underscore (_) instead of a space.
    '''
    # handle a string of less than 2 ladybugs
    if len(s)<2:
        return False

    # handle the string of 2 ladybugs - both must be the same and not a space
    if len(s)==2:
        return s[1]==s[0] and s[1] != ' '

    
    # handle the case of no spaces 
    if s.count(' ') == 0:
        # no spaces, every item must be next to one of the same color
        # so we loop from 1 to len-1 and for each item
        # check the one before and the one after
        # if we ever have an unhappy bug, we can just return False
        for i in range(1,len(s)-1):
            if s[i] != s[i+1] and s[i] != s[i-1]:
                return False

        # if we ever get here every bug has at least one neighbor of the same color
        return True

    # if we get here it means there's at least one space so we can rearrange the bugs
    # however we please so as long as there are at least 2 bugs of each color
    # we can make them all happy

    # replace the spaces with "" since we don't want to count them
    # Since we know they were in the string we can rearrange but
    # they're no longer needed
    s = s.replace(" ","")

    # tally up all the bugs to see if there are at least 2 of each
    bugcounts = {}
    for bug in s:
        bugcounts.setdefault(bug,0) # set to 0 the first time we see this key
        bugcounts[bug]=bugcounts[bug]+1

    
    counts = list(bugcounts.values())

    # if there is any value of 1 in the counts then there's a lone ladybug
    # that can't be made happy
    # so we return True (happy) if there are 0 counts of 1 in our list 
    return counts.count(1) == 0 


bugs="abaccbe ff eggggggg"
print(bugs)
are_happy(bugs)

