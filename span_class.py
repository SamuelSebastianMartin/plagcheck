#! /usr/bin/env python3

import re


class Span:
    """
    A class to find the index span of a string, which regex
    an index slice of a word list.
    i and j are the indices of the list span, para_words
    span is the tuple with the text indices.
    """
    def __init__(self, text, para_words, span):
        self.i = span[0]
        self.j = span[1]
        self.span = self.set_text_span(para_words, text)

    def set_text_span(self, para_words, text):
        expr = r'\W+'.join(para_words[self.i: self.j])
        regx = re.compile(expr, re.IGNORECASE)
        srch = regx.search(text)
        if not srch:
            import pdb;pdb.set_trace()
            raise Exception('Search failed in the text (Span class)')
        else:
            print(srch.group())
            return srch.span()
