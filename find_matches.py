#! /usr/bin/env python3

import logging
logging.basicConfig(level=logging.CRITICAL)

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
    '''When given the index of 2 identical words in sa and rp,
    it goes stepwise through both texts finding the longest series
    of consecutive words which are the same in both texts'''
    for n in range(1, len(sa)-sstart+2):
        # Start = 1 to avoid '[]' as first term.
        # The 'len(sa)...' is to check to the end of the essay, not beyond.
        if sa[sstart:sstart + n] == rp[rstart:rstart + n]:
            pass
        else:
            print('longest = ', sa[sstart:sstart + n-1])
            return sa[sstart:sstart + n-1]

def longstring_only(matches):
    '''Compares 2 lists of words where one is a subset of the other
    and returns the longest of the two
    >>>longstring_only([['a', 'b'],['a']])
    >>>['a', 'b']'''
    logging.debug
    lengths = [len(item) for item in matches]
    logging.debug("lengths: {}".format(lengths))
    lengths.sort()
    logging.debug("lengths.sorted: {}".format(lengths))
    biggest = lengths[-1]
    logging.debug("biggest: {}".format(biggest))
    big = [item for item in matches if len(item) == biggest]
    logging.debug("big: {}".format(big))
    return big[0]  # To avoid identical pairs


def find_matches(rp, sa):
    '''Goes through each word in sa, and returns a list of
    all phrases which also appear in rp'''

    pointer = 0  # Pointer shows position in sa.
    matches = []
    all_matches = []
    while pointer < len(sa)-2:
        word = sa[pointer]
        logging.debug("pointer: {}, word: {}".format(pointer, word))
        rp_occurrences = find_occurrences(word, rp)
        logging.debug('Occurrences in rp = {}'.format(rp_occurrences))
        if rp_occurrences != []:
            logging.debug("Word = {} occurrences = {}".format(word, rp_occurrences))
            matches = [longest_match(rp, sa, index, pointer)
                    for index in rp_occurrences]
            matches = longstring_only(matches)
            logging.debug("matches: {}".format(matches))
            all_matches.append(matches)
            #  Move sa pointer to end of this matched phrase.
            pointer += len (matches)
        else:
            pointer += 1
    logging.debug('\n all_matches = {}'.format(all_matches))
    return all_matches


if __name__ == '__main__':
    find_matches(rp, sa)
