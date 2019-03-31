#! /usr/bin/env python3

import re


class Match:

    def __init__(self, i, para_words, text):
        self.i = i
        self.j = i + 1  # 3 is the minimum word match requirement.
        self.regex = self.get_regex(para_words)
        self.found = self.search(text)

    def get_regex(self, para_words):
        """produces the regex search for any span in para_words"""
        str = r'\W+'.join(para_words[self.i : self.j])
        expr = re.compile(str, re.IGNORECASE)
        return expr

    def search(self, text):
        srch = self.regex.search(text)
        return srch


def test():
    a = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    b = 'three four five'
    match = Match(2, a, b)

    if match.found:
        print('found', match.found.group())


if __name__ == '__main__':
    test()
