#!/usr/bin/env python3

# early development of part of the
# find_matches() fn for the plagiarism
# checker.

#def find_occurrences(word, text): # working
#    '''finds the string indexes for every
#    occurrence of the word in the text, and
#    returns them as a list'''
#    occurrences = []
#    n = text.count(word)
#    m = 0
#    for i in range(n): # only look n times
#        occurrence = text.find(word, m) # start at m
#        occurrences.append(occurrence)
#        m = occurrence + 1
#    return occurrences
#
#sa_occurrences = find_occurrences(word, text)
#print(sa_occurrences)

word = 'quick'
rp = 'the quick brown fox'
sa = 'quick brown'
rp_occur = 4
sa_occur = 0
str_length = 5

def find_longest_match(rp, sa, rp_occur, sa_occur, str_length):
    '''if passed the string index of a word in both
    the sa and the rp, it will find and return the 
    longest matching string begining at those points'''
    while sa[sa_occur:sa_occur + str_length] == rp[rp_occur:rp_occur + str_length]:
        match = sa[sa_occur:sa_occur + str_length]
        str_length += 2 # should still catch whole words if not 1
        print('Match = ', match) # test only #
    return match
longest_match = find_longest_match(rp, sa, rp_occur, sa_occur, len(word))
print('The longest matching phrase is: ', longest_match)
