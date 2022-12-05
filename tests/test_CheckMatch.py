#! /usr/bin/env/ python3

import unittest

import CheckMatch as Ch


class TestRegex(unittest.TestCase):

    def test_double_space_haystack(self):
        needle = "one two"
        haystack = "  one   two    many spaces"
        self.assertTrue(Ch.CheckMatch(needle, haystack))

    def test_double_space_needle(self):
        needle = "   one      two   "
        haystack = "one two"
        self.assertTrue(Ch.CheckMatch(needle, haystack))

    def test_punctuation_needle(self):
        needle = ",!one,' %& +-two"
        haystack = "one two"
        self.assertTrue(Ch.CheckMatch(needle, haystack))

    def test_punctuation_haystack(self):
        needle = "one two"
        haystack = ",!one,' %& +-two"
        self.assertTrue(Ch.CheckMatch(needle, haystack))

if __name__ == '__main__':
    unittest.main()
