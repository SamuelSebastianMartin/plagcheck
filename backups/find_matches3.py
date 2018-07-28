#!/usr/bin/env python3

# early development of part of the
# find_matches() fn for the plagiarism
# checker.
import time
rp = 'the quick brown fox jumped over the lazy lazy dog dog dog'
sa = 'quick brown lazy dog quick dog'
unique_words = ['quick', 'brown', 'lazy', 'dog']


def find_matches(rp, sa, unique_words):
    """ for each unique word:
           for each occurance of word in sa:
               for each occurance of word in rp:
                   check for matches in texts.    """
    
    def find_longest_match(rp, sa, rp_occur, sa_occur, str_length): # working
        '''if passed the string index of a word in both
           the sa and the rp, it will find and return the 
           longest matching string begining at those points'''
        while sa[sa_occur:sa_occur + str_length] == rp[rp_occur:rp_occur + str_length]:
            time.sleep(1)
            print('sa string = ', sa[sa_occur:sa_occur + str_length]) # test only
            print('rp string = ', rp[rp_occur:rp_occur + str_length]) # test only
            match = sa[sa_occur:sa_occur + str_length]
            str_length += 2 # should still catch whole words if not 1
            if match == sa[sa_occur:sa_occur + str_length]:
                break # avoid infinite loop at end of strings
            else:
                print('Match = ', match) # test only #
        return match
    
    def find_occurrences(word, text): # working
        ''' finds the string indexes for every
        occurrence of the word in the text, and
        retcurns them as a list'''
        occurrences = []
        n = text.count(word)
        m = 0
        for i in range(n): # only look n times
            occurrence = text.find(word, m) # start at m
            occurrences.append(occurrence)
            m = occurrence + 1
        return occurrences

    duplicates_list = []
    for word in unique_words:
        sa_occurrences = find_occurrences(word, sa)
        print(word) # test only
        print('sa_occurrences = ', sa_occurrences) # test only
        for sa_occur in sa_occurrences:
            rp_occurrences = find_occurrences(word, rp)
            print('rp_occurrences = ', rp_occurrences) # test only
            for rp_occur in rp_occurrences:
                match = find_longest_match(rp, sa, rp_occur, sa_occur, len(word))
            duplicates_list.append(match)
    return duplicates_list

    
duplicates_list = find_matches(rp, sa, unique_words)
print(duplicates_list)
