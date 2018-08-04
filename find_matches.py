#! /usr/bin/env python3

import logging
logging.basicConfig(level=logging.DEBUG)

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

def longest_match(rp, sa, rstart, sstart):
    for n in range(1, len(sa)-sstart+2):
        # Start = 1 to avoid '[]' as first term.
        # The 'len(sa)...' is to check to the end of the essay, not beyond.
        if sa[sstart:sstart + n] == rp[rstart:rstart + n]:
            pass
        else:
            print('longest = ', sa[sstart:sstart + n-1])
            return sa[sstart:sstart + n-1]

def longstring_only(matches):
    lengths = [len(item) for item in matches]
    logging.debug("lengths: {}".format(lengths))
    lengths.sort()
    logging.debug("lengths.sorted: {}".format(lengths))
    biggest = lengths[-1]
    logging.debug("biggest: {}".format(biggest))
    big = [item for item in matches if len(item) == biggest]
    logging.debug("big: {}".format(big))
    longest_item = big[0]  # To avoid identical pairs
    logging.debug("longest_item: {}".format(longest_item))


def find_matches(rp, sa):
    pointer = 0  # Pointer shows position in sa.
    while pointer < len(sa):
        word = sa[pointer]
        rp_occurrences = find_occurrences(word, rp)
        if rp_occurrences != []:
            print(word, rp_occurrences)
            matches = [longest_match(rp, sa, index, pointer)
                    for index in rp_occurrences]
            print('matches list: ', matches)
        pointer += 1

rp = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'two', 'three', 'six']
sa = ['two', 'three', 'four', 'six', 'ninty']

if __name__ == '__main__':
    find_matches(rp, sa)
