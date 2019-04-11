#! /usr/bin/env python3

import re

class Count:
    """Using a class for the indexes 'i' and 'j' keeps track
    through the recursion, which does not exit once it reaches
    the 'return' line."""
    def __init__(self, i):
        self.i = i
        self.j = i + 1

def check_match(sliced, text):
    """
    Checks a slice of para_words against the text.
    Returns re.seach object, to evaluate as True or False.
    """
    expr = r'\W+'.join(sliced)
    regx = re.compile(expr, re.IGNORECASE)
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
            return (ct.i, ct.j-1)  # -1 cos j was ++ once too often


def find_matches(text, words):
    """
    Takes a text and list of words and, starting from each word
    successively, it finds the longest slice of the list which
    is matched in the text. It returns a list of tuples, each
    representing the start and end of the longest span from
    each word
    """
    spans = []
    for i in range(len(words)):
        ct = Count(i)
        recursive_search(words, text, ct)
        span = (ct.i, ct.j)
        spans.append(span)
    return spans

#def test():
#    """
#    Leave this commented out to avoid these local values
#    for 'words' and 'text' overriding the genuine input
#    """
#    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
#    text = 'one two three four five six'
#    spans = find_matches(text, words)
#    print(spans)
#
#
#if __name__ == '__main__':
#    test()
