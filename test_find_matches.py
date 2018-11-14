#! /usr/bin/env/ python3

import re
import unittest
import find_matches


class TestAdd(unittest.TestCase):

    def test_compile_regex1(self):
        #  ignores case and punctuation, and finds only
        #  matches from index i
        i = 0
        j = 2
        para_words = ['the', 'end', 'of', 'as', 'we', 'know']
        rp = '(The, end. as we know it'

        expr = find_matches.complie_regex(i, j, para_words)
        mo = expr.search(rp)
        result = mo.group()
        self.assertEqual(result, 'The, end')

    def test_compile_regex2(self):
        #  finds onl matches from index i, not [0]
        i = 4
        j = 2
        para_words = ['the', 'end', 'of', 'as', 'we', 'know']
        rp = '(The, end. as we know it'

        expr = find_matches.complie_regex(i, j, para_words)
        mo = expr.search(rp)
        result = mo.group()
        self.assertEqual(result, 'we know')

    def test_match_status1(self):
        #  Checks that match -> True
        i = 0
        j = 1
        matches = []
        para_words = ['the', 'end']
        rp = 'the end'

        result = find_matches.match_status(i, j, para_words, rp)
        self.assertEqual(result, True)

    def test_match_status2(self):
        #  Checks that no match -> not True
        i = 0
        j = 1
        matches = []
        para_words = ['the', 'end']
        rp = 'fuck me'

        result = find_matches.match_status(i, j, para_words, rp)
        self.assertNotEqual(result, True)

#    def test_longest_match1(self):
#        #  finds onl matches from index i, not [0]
#        i = 4
#        para_words = ['the', 'end', 'of', 'as', 'we', 'know']
#        rp = '(The, end. as we know it'
#        matches = []
#
#        result = find_matches.longest_match(i, matches, para_words, rp)
#        self.assertEqual(result, 'we know')


if __name__ == '__main__':
    unittest(main)
