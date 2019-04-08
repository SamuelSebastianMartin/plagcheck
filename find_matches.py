#! /usr/bin/env python3

import re
import logging

class Count:
    def __init__(self, i, j):
        self.i = i
        self.j = j

def check_match(sliced, text):
    """
    Checks a slice of para_words against the text.
    Returns re.seach object, to evaluate as True or False.
    """
    expr = r'\W+'.join(sliced)
    regx = re.compile(expr)
    srch = regx.search(text)
    return srch

def recursive_search(words, text, ct):
    if not check_match(words[ct.i:ct.j], text):
        return (ct.i, ct.j)
    else:
        ct.j += 1
        if ct.j < len(words):
            recursive_search(words, text, ct)
        else:
            # If end of 'words' list reached.
            return (ct.i, ct.j)


def main():
    para_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    rp = 'one two three four five six'
    matches = []
    ct = Count(1, 3)
    recursive_search(para_words, rp, ct)
    span = (ct.i, ct.j - 1)
    print(span)


if __name__ == '__main__':
    main()
