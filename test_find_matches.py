#! /usr/bin/env/ python3

import re
import unittest
import find_matches


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.para_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
        self.rp = 'one two three four five six'
        self.matches = []

    def test_check_match1(self):
        """A good match returns True."""
        sliced = self.para_words[1:4]
        match = find_matches.check_match(sliced, self.rp)
        self.assertTrue(match)

    def test_check_match2(self):
        """A bad match returns False."""
        sliced = self.para_words[0:4]
        match = find_matches.check_match(sliced, self.rp)
        self.assertFalse(match)

    def test_recursive_search(self):
        span = find_matches.recursive_search(self.para_words, self.rp, 0, 3)
        print(span)

if __name__ == '__main__':
    unittest.main()
