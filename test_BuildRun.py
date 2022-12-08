#! /usr/bin/env/ python3

import unittest
from BuildRun import BuildRun

orig = "the quick brown fox"
para = "quick brown cat" # one paragraph (précis of the original text).

class TestBuildRun(unittest.TestCase):

    def test_next_whitespace1(self):
        run1 = BuildRun(para, orig, 0)
        space1 = run1.next_whitespace()
        self.assertEqual(space1, 6)

#        run2 = BuildRun(para, orig, 6)
#        space2 = run1.next_whitespace()
#        self.assertEqual(space2, 12)

if __name__ == '__main__':
    unittest.main()
