#! /usr/bin/env/ python3

import unittest
from BuildRun import BuildRun

orig = "the quick brown fox"
para = "quick brown cat" # one paragraph (précis of the original text).

class TestBuildRun(unittest.TestCase):

    def test_next_word1(self):
        run1 = BuildRun(para, orig, 0)
        space1 = run1.next_word()
        self.assertEqual(space1, 6)

#        space2 = run1.next_word()
#        self.assertEqual(space2, 12)

if __name__ == '__main__':
    unittest.main()
