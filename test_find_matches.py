#! /usr/bin/env/ python3

import re
import unittest
import find_matches


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.para_words = ['the', 'end', 'of', 'as', 'we', 'know', '_dummy_']
        self.rp = '(The, end. as we know it'
        self.matches = []

    def test_compile_regex1(self):
        #  ignores case and punctuation, and finds only
        #  matches from index i
        i = 0
        j = 2

        expr = find_matches.compile_regex(i, j, self.para_words)
        mo = expr.search(self.rp)
        result = mo.group()
        self.assertEqual(result, 'The, end')

    def test_compile_regex2(self):
        #  finds only matches from index i, not [0]
        i = 4
        j = 2

        expr = find_matches.compile_regex(i, j, self.para_words)
        mo = expr.search(self.rp)
        result = mo.group()
        self.assertEqual(result, 'we know')

    def test_compile_regex3(self):
        #  functions at end of strings and end of para_words.
        i = 4
        j = 2
        self.rp = '(The, end. as we know'

        expr = find_matches.compile_regex(i, j, self.para_words)
        mo = expr.search(self.rp)
        result = mo.group()
        self.assertEqual(result, 'we know')

    def test_longest_match1(self):
        #  finds onl matches from index i, not [0]
        i = 4

        result = find_matches.longest_match(i, self.para_words, self.rp)
        answer = re.compile('we\\W+know', re.IGNORECASE)
        self.assertEqual(result, answer)

    def test_filter_empties(self):
        matches =  [re.compile('', re.IGNORECASE), None, None, None]
        answer = []
        result = find_matches.filter_empties(matches)
        self.assertEqual(result, answer)

    def test_find_matches(self):
        pass

if __name__ == '__main__':
    unittest.main()
