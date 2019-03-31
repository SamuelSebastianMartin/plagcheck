#! /usr/bin/env python3

import unittest
from match_class import Match

class TestMatch(unittest.TestCase):

    def setUp(self):
        self.rp = "One two. Three four five six seven eight."
        para_words = ['three', 'four', 'five', 'six']
        self.sa = "Three four: five six?"

    def test_get_regex(self):
        result = Match.get_regex(self, (0, 3), self.para_words)
        answer = re.compile('three\W+four\W+five', re.IGNORECASE)
        self.assertEqual(result, answer)
