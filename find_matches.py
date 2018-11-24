#! /usr/bin/env python3

import re
import logging

logging.basicConfig(level=logging.DEBUG)

#  Data for testing only.
para_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', '_dummy_']
rp = 'One, two (three) five. Six!'
match = ''
#  End test data.

print("para_words: {}".format(para_words))#
print("        rp: {}\n".format(rp))#


def find_matches(rp, para_words):
    matches = []  # _SRE_Pattern objects.
    i = 0
    while i < len(para_words):
        print("\nNew loop. i = ", i)#
        match = longest_match(i, para_words, rp)
        matches.append(match)
        print('>>>', match, 'appended to ', matches)#
        i += 1
    print('matches = ', matches)#
    matches = filter_empties(matches)
    for match in matches:
        print(match)#
        match.search(rp)
    return matches


def filter_empties(matches):
    '''removes instances of 'None', which would crash in a 'search'.
    For some reason, it leaves one 'None' behind, so must run twice!?!'''
    real_matches = []
    for match in matches:
        print('index =', matches.index(match), 'noneLoop =', match)#
        if match != None:
            real_matches.append(match)
        else:
            continue

    empty = re.compile('', re.IGNORECASE)
    non_empty = []
    for match in real_matches:
        if match != empty:
            non_empty.append(match)
    print(non_empty)#
    return non_empty


def longest_match(i, para_words, rp):
    '''
    Starting from the word at index [i], it keeps adding words from
    the para_words list til the longest match is found with the rp.
    Returns a regex expression.
    '''
    match = compile_regex(0, 0, [''])  # To declare 'match'
    for j in range (1, len(para_words) ):  # ie. remainder of list.
        print('i = ', i, 'j = ', j)#
        expr = compile_regex(i, j, para_words)

        print('compile received = ', expr)#
        search_result = expr.findall(rp)
        if search_result == []:
            print('returning match: ', match)
            return match
        match = expr


def compile_regex(i, j, para_words):
    '''produces the regex search to be check against the rp'''
    str = r'\W+'.join(para_words[i: i+j])
    expr = re.compile(str, re.IGNORECASE)
    print('<compile_regex> returns ', expr)#
    return expr


if __name__ == '__main__':
    find_matches(rp, para_words)
