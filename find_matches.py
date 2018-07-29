#! /usr/bin/env python3

def longest(rp, sa, rp_occur, sa_occur):
    '''if passed the index of a word in both
       the sa and the rp, it will find and return the 
       longest matching string begining at those points'''
    m = 1
    while sa[sa_occur:sa_occur + m] == rp[rp_occur:rp_occur + m]:
        match = sa[sa_occur:sa_occur + m]
        m += 1
        if match == sa[sa_occur:sa_occur + m]:
            break  # Avoid infinite loop at end of strings.
    return match
    
def find_occurrences(word, text):
    ''' finds the indexes for every
    occurrence of the word in the text, and
    retcurns them as a list'''
    occurrences = []
    n = text.count(word)
    m = 0
    for i in range(n):  # Only look n times.
        occurrence = text.index(word, m)  # Start at m.
        occurrences.append(occurrence)
        m = occurrence + 1
    return occurrences





def find_matches(rp, sa, wordset):
    """ for each unique word:
           for each occurance of word in sa:
               for each occurance of word in rp:
                   check for matches in texts.    """
    # This should change, perhaps with a check forward/backwards counter
    # e.g.  m += n, where n is + or - 1 word. This will allow the capture
    # of words like 'the' or 'an' before the words in 'wordset', once it
    # has been stripped of stop-words.
    duplicates_list = []
    for word in wordset:
        sa_occurrences = find_occurrences(word, sa)
        for sa_occur in sa_occurrences:
            rp_occurrences = find_occurrences(word, rp)
            match = []  # ?
            for rp_occur in rp_occurrences:
                match = longest(rp, sa, rp_occur, sa_occur) 
            duplicates_list.append(match)
    return duplicates_list


if __name__ == '__main__':
    find_matches(rp, sa, wordset)
