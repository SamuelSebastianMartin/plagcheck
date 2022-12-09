#! /usr/bin/env/ python3

import unittest
from Run import Run

orig = "the quick brown fox"
para = "quick brown cat" # one paragraph (précis of the original text).

class TestRun(unittest.TestCase):

    def test_init_(self):
        run = Run(orig, para, 0)
        self.assertEqual(run.i, 0)

    def test_add_word1(self):
        run = Run(orig, para, 0)
        run.add_word()
        self.assertNotEqual(run.lastWordLen, 0)
        self.assertIn('quick', run.currentRegex)
        self.assertNotIn('brown', run.currentRegex)

    def test_add_word2(self):
        run = Run(orig, para, 6)
        run.add_word()
        self.assertNotEqual(run.lastWordLen, 0)
        self.assertIn('brown', run.currentRegex)
        self.assertNotIn('quick', run.currentRegex)

    def test_search_for_match1(self):
        run = Run(orig, para, 0)
        run.add_word()
        result = run.search_for_match()
        self.assertTrue(result)

    def test_search_for_match2(self):
        run = Run(orig, para, 12) # 'cat' not in orig
        run.add_word()
        result = run.search_for_match()
        self.assertFalse(result)

    def test_build_run1(self):
        run = Run(orig, para, 0)
        run.build_run()
        self.assertEqual(run.run, 'quick brown')

    def test_build_run2(self):
        run = Run(orig, 'quick cat', 0)
        run.build_run()
        self.assertEqual(run.run, 'quick')

    def test_build_run3(self):
        run = Run(orig, 'fox', 0)
        run.build_run()
        self.assertEqual(run.run, 'fox')

if __name__ == '__main__':
    unittest.main()
