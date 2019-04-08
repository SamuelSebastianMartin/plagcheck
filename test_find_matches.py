#! /usr/bin/env/ python3

import re
import unittest
import find_matches


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.para_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
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

    def test_recursive_search1(self):
        """Find match in middle of para_words"""
        ct = find_matches.Count(1)  # Start search at (1, 3)
        find_matches.recursive_search(self.para_words, self.rp, ct)
        span = (ct.i, ct.j - 1)
        self.assertEqual(span, (1, 7))

    def test_recursive_search2(self):
        """No match at start of para_words"""
        ct = find_matches.Count(0)  # Start search at (1, 3)
        find_matches.recursive_search(self.para_words, self.rp, ct)
        span = (ct.i, ct.j - 1)
        self.assertEqual(span, (0, 0))

    def test_recursive_search2a(self):
        """No match in middle of para_words"""
        self.rp = 'one three four'
        ct = find_matches.Count(2)  # Start search at (1, 3)
        find_matches.recursive_search(self.para_words, self.rp, ct)
        span = (ct.i, ct.j - 1)
        self.assertEqual(span, (2, 2))

    def test_recursive_search3(self):
        """Single word match"""
        ct = find_matches.Count(6)  # Start search at (1, 3)
        find_matches.recursive_search(self.para_words, self.rp, ct)
        span = (ct.i, ct.j - 1)
        self.assertEqual(span, (6, 7))

    def test_recursive_search4(self):
        """Match at end of rp and para_words"""
        self.para_words = ['zero', 'one', 'two', 'three', 'four', 'five']
        self.rp = 'one two three four five'
        ct = find_matches.Count(3)  # Start search at (1, 3)
        find_matches.recursive_search(self.para_words, self.rp, ct)
        span = (ct.i, ct.j - 1)
        self.assertEqual(span, (3, 5))


if __name__ == '__main__':
    unittest.main()
