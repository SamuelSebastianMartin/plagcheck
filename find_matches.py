#! /usr/bin/env python3


def find_occurrences(word, text): # working
    ''' finds the indexes for every
    occurrence of the word in the text, and
    retcurns them as a list'''
    occurrences = []
    n = text.count(word)
    m = 0
    for i in range(n): # only look n times
        occurrence = text.index(word, m) # start at m
        occurrences.append(occurrence)
        m = occurrence + 1
    return occurrences

def longest(rp, sa, rstart, sstart):
    for n in range(1, len(sa)-sstart+2):
        # Start = 1 to avoid '[]' as first term.
        # The 'len(sa)...' is to check to the end of the essay, not beyond.
        if sa[sstart:sstart + n] == rp[rstart:rstart + n]:
            pass
        else:
            print('longest = ', sa[sstart:sstart + n-1])
            return sa[sstart:sstart + n-1]

def find_matches(rp, sa):
    pointer = 0  # Pointer shows position in sa.
    while pointer < len(sa):
        word = sa[pointer]
        rp_occurrences = find_occurrences(word, rp)
        print(word, rp_occurrences)
        matches = []
        for index in rp_occurrences:
            match = longest(rp, sa, index, pointer)
            matches.append(match)
        print('matches list: ', matches)
        pointer += 1

rp = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'two', 'three', 'six']
sa = ['two', 'three', 'four', 'six', 'ninty']

if __name__ == '__main__':
    find_matches(rp, sa)
