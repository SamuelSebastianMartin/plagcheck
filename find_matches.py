#! /usr/bin/env python3

import re
import logging

logging.basicConfig(level=logging.DEBUG)

#  Data for testing only.
para_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
rp = 'one two three four five six'

print(rp)###
print(para_words)###

def find_matches(rp, para_words):
    """
    Runs through the list of para_words. For each word, it joins successive
    words into a phrase, and checks to see if it matches any phrases in the rp.
    For each match, the span of the match is saved (ie, the span in para_words.
    It returns a list of spans, which will contain overlaps.
    Non matches are recorded as a (0, 0) span.
    """
    matches = []  # Spans in para_words list.
    i = 0
    while i < len(para_words):
        match = longest_match(i, para_words, rp)
        matches.append(match)
        print(match)###
        print(matches)###
        i += 1
    return matches  #c Now a list of spans.


def longest_match(i, para_words, rp, min_wrds=3):
    """
    Starting from the word at index [i], it keeps adding words from
    the para_words list til the longest match is found with the rp.
    Returns a list of spans in para_words for each matched section.
    Warning: there will be overlaps in the spans which are returned.
    """
    span = (0, 0)

    for j in range (i, len(para_words) + 1 ):  # ie. remainder of list.
        print('span at start of longest_match:', span)
        expr = compile_regex(i, j, para_words)
        search_result = expr.search(rp)
        print(i, j, search_result, expr)###
        if not search_result:
            print('no match. span = ', span)###
            return span
        elif i + j >= len(para_words) + 1:
            print('length exceded para_words', span)
            return span
        else:
            span = (i, j)
            print('match. span =', span)###


def compile_regex(i, j, para_words):
    """produces the regex search to be check against the rp"""
    str = r'\W+'.join(para_words[i: j])
    expr = re.compile(str, re.IGNORECASE)
    return expr


if __name__ == '__main__':
    find_matches(rp, para_words)
