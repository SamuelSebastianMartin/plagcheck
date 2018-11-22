#! /usr/bin/env/ python3

import re
import unittest
import find_matches


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.para_words = ['the', 'end', 'of', 'as', 'we', 'know']
        self.rp = '(The, end. as we know it'
        self.matches = []

    def test_compile_regex1(self):
        #  ignores case and punctuation, and finds only
        #  matches from index i
        i = 0
        j = 2

        expr = find_matches.complie_regex(i, j, self.para_words)
        mo = expr.search(self.rp)
        result = mo.group()
        self.assertEqual(result, 'The, end')

    def test_compile_regex2(self):
        #  finds only matches from index i, not [0]
        i = 4
        j = 2

        expr = find_matches.complie_regex(i, j, self.para_words)
        mo = expr.search(self.rp)
        result = mo.group()
        self.assertEqual(result, 'we know')

    def test_compile_regex3(self):
        #  functions at end of strings and end of para_words.
        i = 4
        j = 2
        self.rp = '(The, end. as we know'

        expr = find_matches.complie_regex(i, j, self.para_words)
        mo = expr.search(self.rp)
        result = mo.group()
        self.assertEqual(result, 'we know')

    def test_match_status1(self):
        #  Checks that match -> True
        i = 0
        j = 1
        self.para_words = ['the', 'end']
        self.rp = 'the end'

        result = find_matches.match_status(i, j, self.para_words, self.rp)
        self.assertEqual(result, True)

    def test_match_status2(self):
        #  Checks that no match -> not True
        i = 0
        j = 1
        self.matches = []
        self.para_words = ['the', 'end']
        self.rp = 'fuck me'

        result = find_matches.match_status(i, j, self.para_words, self.rp)
        self.assertNotEqual(result, True)

    def test_longest_match1(self):
        #  finds onl matches from index i, not [0]
        i = 4

        match = find_matches.longest_match(i, self.para_words, self.rp)
        mo = match.search(self.rp)
        result = mo.group()
        self.assertEqual(result, 'we know')


if __name__ == '__main__':
    unittest.main()
