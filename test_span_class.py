#! /usr/bin/env python3

import unittest
from span_class import Span

class TestSpan(unittest.TestCase):

    def setUp(self):
        self.para_words = ['three', 'four', 'five', 'six']
        self.text = "Three four: five six?"

    def test_get_regex1(self):
        sp = Span(self.text, self.para_words, (1, 3))
        result = sp.span()
        answer = (6, 16)
        self.assertEqual(result, answer)

    def test_get_regex2(self):
        sp = Span(self.text, self.para_words, (0, 4))
        result = sp.span()
        answer = (0, 20)
        self.assertEqual(result, answer)
