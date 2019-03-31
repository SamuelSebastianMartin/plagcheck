#! /usr/bin/env python3

import re


class Match:

    def __init__(self, i, para_words, text):
        self.i = i
        self.j = i + 1
        self.regex = self.get_regex(para_words)
        self.found = self.search(text)
        self.longest_span = self.get_longest_span(para_words, text)

    def get_regex(self, para_words):
        """produces the regex search for any span in para_words"""
        str = r'\W+'.join(para_words[self.i : self.j])
        expr = re.compile(str, re.IGNORECASE)
        return expr

    def search(self, text):
        srch = self.regex.search(text)
        return srch

    def get_longest_span(self, words, text):
        if not self.found:
            print('not found', self.j)
            return (self.i, self.j-1)
        else:
            print('Found: ', self.found.span())
            self.j += 1
#            import pdb; pdb.set_trace()
            if self.j < len(words)+1:
                print('OK', self.j)
                self.get_longest_span(words, text)  # Recursive
            else:
                print('end of file')
                return (self.i, self.j-1)

def test():
    a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']
    b = 'three four five'
    match = Match(3, a, b)

    if match.found:
        print('found', match.found.group())
    print(match.i, match.j)

if __name__ == '__main__':
    test()
