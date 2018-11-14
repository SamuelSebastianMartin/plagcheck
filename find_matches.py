#! /usr/bin/env python3

import re
import logging

logging.basicConfig(level=logging.DEBUG)

#  Data for testing only.
para_words = ['the', 'end', 'of', 'as', 'we', 'know']
rp = '(The, end. as we know it'
match = ''
#  End test data.


def find_matches(rp, para_words):
    matches = []  # _SRE_Pattern objects. Must 'search' & 'group'.
    i = 0
    while i < len(para_words):
        match = longest_match(i, para_words, rp)
        matches.append(match)
        i += 1
    for match in matches:
        if type(match) is not None:
            srch = match.search(rp)
            text = srch.group()
            print(text)


def longest_match(i, para_words, rp):
    '''
    Starting from the word at index [i], it
    keeps adding words from the para_words list
    until the longest match is found with the rp.
    '''
    j = 1  # Later this could be a 'sensitivity-level' cut-off.

    #  Sentinel test: Is regex in rp?
    expr = complie_regex(i, j, para_words)
    search_result = expr.search(rp)
    match = expr  # To return if no more matches found in loop.
    if search_result is not None:
        while i + j < len(para_words):
            j += 1
            expr = complie_regex(i, j, para_words)
            match = expr
            search_result = expr.search(rp)
            if search_result is not None:
                break
    return match


def match_status(i, j, para_words, rp):
    #  Redundant if using regex in 'match' & 'matches'.
    '''A function to ward off crashes by allowing a more robust
    sentinel test before loops and conditionals.'''
    expr = complie_regex(i, j, para_words)
    search_result = expr.search(rp)
    if search_result is not None:
        return True


def complie_regex(i, j, para_words):
    '''produces the regex search to be check against the rp'''
    str = r'\W+'.join(para_words[i: i+j])
    expr = re.compile(str, re.IGNORECASE)
    return expr


def main():
    find_matches(rp, para_words)


if __name__ == '__main__':
    main()
