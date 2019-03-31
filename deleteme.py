#! /usr/bin/env python3
import re

para_words = ['one', 'two', 'three', 'four', 'five', 'six']
rp = 'the quick brown two three four five fox jumped five six'
min_wrds = 3


def compile_regex(i, j, para_words):
    """produces the regex search to be check against the rp"""
    str = r'\W+'.join(para_words[i: i+j])
    expr = re.compile(str, re.IGNORECASE)
    return expr


for i in range(6):
    span = ()
    print('i =', i)
    for j in range (i + min_wrds, len(para_words) ):  # ie. remainder of list.
        print('j =', j)
        expr = compile_regex(i, j, para_words)
        print('expr = ', expr)
        search_result = expr.search(rp)
        print('search_result =', search_result)
        if search_result:
            span = (i, j)
            print('match. span =', span)
        else:
            print('no match. span = ', span)
            break
