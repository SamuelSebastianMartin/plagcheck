#i+! /usr/bin/env python3

import re
import logging

logging.basicConfig(level=logging.DEBUG)

#  Data for testing only.
para_words = ['the', 'end', 'as', 'of', 'as', 'we', 'know']
rp = '(The, end. as we know it'
match = ''
#  End test data.

print("para_words: {}".format(para_words))#
print("        rp: {}\n".format(rp))#

def find_matches(rp, para_words):
    matches = []  # Sequence of _SRE_Pattern objects. Must 'search' & 'group'.
    i = 0
    while i < len(para_words):
        print("\nNew loop. i = ", i)#
        match = longest_match(i, para_words, rp)
        matches.append(match)
        print('matches = ', matches)#
        i += 1
    print('matches = ', matches)#
    for match in matches:
        if type(match) is not None:
            print('type(match) = ', type(match))#
#            srch = match.search(rp)
#            text = srch.group()
#            print(text)#


def longest_match(i, para_words, rp):
    '''
    Starting from the word at index [i], it
    keeps adding words from the para_words list
    until the longest match is found with the rp.
    Returns a regex expression.
    '''
    match = compile_regex(i, 1, para_words)  # To declare 'match'
    for j in range (1, len(para_words) -i):  # ie. remainder of list.
        print('i = ', i, 'j = ', j)#
        expr = compile_regex(i, j, para_words)

        print('compile received = ', expr)#
        search_result = expr.findall(rp)
        if search_result == [] :
            return match
        match = expr


def match_status(i, j, para_words, rp):
    #  Redundant if using regex in 'match' & 'matches'.
    '''A function to ward off crashes by allowing a more robust
    sentinel test before loops and conditionals.'''
    expr = compile_regex(i, j, para_words)
    search_result = expr.findall(rp)
    if search_result != [] :
        return True


def compile_regex(i, j, para_words):
    '''produces the regex search to be check against the rp'''
    str = r'\W+'.join(para_words[i: i+j])
    expr = re.compile(str, re.IGNORECASE)
    print('<compile_regex> returns {}', expr)#
    return expr


def main():
    pass
#    find_matches(rp, para_words)


if __name__ == '__main__':
    find_matches(rp, para_words)
