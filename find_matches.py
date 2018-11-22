#! /usr/bin/env python3

import re
import logging

logging.basicConfig(level=logging.CRITICAL)

#  Data for testing only.
para_words = ['the', 'end', 'of', 'as', 'we', 'know']
rp = '(The, end. as we know it'
match = ''
#  End test data.

logging.debug("para_words: {}".format(para_words))
logging.debug("        rp: {}".format(rp))

def find_matches(rp, para_words):
    matches = []  # Sequence of _SRE_Pattern objects. Must 'search' & 'group'.
    i = 0
    while i < len(para_words):
        logging.debug("New loop. i = {}".format(i))
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
    Returns a regex expression.
    '''
    for j in range (len(para_words)-i):  # ie. remainder of list.
        logging.debug('<longest_match> {}-word: {}'.format(j, para_words[i: i+j]))
        expr = complie_regex(i, i+j, para_words)
        match = expr
        search_result = expr.search(rp)
        if search_result is None:
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
    print('<compile_regex> returns {}'.format(expr))
    return expr


def main():
    pass
#    find_matches(rp, para_words)


if __name__ == '__main__':
    find_matches(rp, para_words)
