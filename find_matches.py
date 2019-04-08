#! /usr/bin/env python3

import re

class Count:
    """Using a class for the indexes 'i' and 'j' keeps track
    through the recursion, which does not exit once it reaches
    the 'return' line."""
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
    """
    Given a starting point, 'i', this function tests successively
    increasing slices [i:j] of the words list. Returned values are
    misleading, so the results are read outside the function
    from the Count class 'ct.i' and 'ct.j'.
    """

    if not check_match(words[ct.i:ct.j], text):
        # When match fails.
        return (ct.i, ct.j)
    else:
        # Increment j and rerun funtion recursively.
        ct.j += 1
        if ct.j < len(words):
            recursive_search(words, text, ct)
        else:
            # If end of 'words' list reached.
            return (ct.i, ct.j)


def test():
    para_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    rp = 'one two three four five six'
    matches = []
    ct = Count(1, 3)
    recursive_search(para_words, rp, ct)
    span = (ct.i, ct.j - 1)
    print(span)


if __name__ == '__main__':
    test()
