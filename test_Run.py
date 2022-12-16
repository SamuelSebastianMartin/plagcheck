#! /usr/bin/env/ python3

import unittest
from Run import Run

orig = "the quick brown fox"
para = "quick brown cat" # one paragraph (précis of the original text).

class TestRun(unittest.TestCase):

    def test_init_(self):
        run = Run(orig, para, 0)
        self.assertEqual(run.i, 0) # _init_ has run

    def test_add_word1(self):
        run = Run(orig, para, 0)
        run.add_word()
        self.assertNotEqual(run.lastWordLen, 0) # a word is added
        self.assertIn('quick', run.currentRegex) # word is correct
        self.assertNotIn('brown', run.currentRegex) # only one word

    def test_add_word2(self):
        run = Run(orig, para, 6) # start not at beginning
        run.add_word()
        self.assertNotEqual(run.lastWordLen, 0) # a word is added
        self.assertIn('brown', run.currentRegex) # word is correct
        self.assertNotIn('quick', run.currentRegex) # only one word

    def test_search_for_match1(self):
        run = Run(orig, para, 0)
        run.add_word()
        result = run.search_for_match()
        self.assertTrue(result) # search is successful

    def test_search_for_match2(self):
        run = Run(orig, para, 12) # 'cat' not in orig
        run.add_word()
        result = run.search_for_match()
        self.assertFalse(result)

    def test_build_run1(self):
        run = Run(orig, para, 0)
        run.build_run()
        self.assertEqual(run.run, 'quick brown') # finds correct text
        self.assertTrue(run.category[0]) # Labels as 'True'

    def test_build_run2(self):
        run = Run(orig, 'quick cat', 0) # 'cat' not in orig
        run.build_run()
        self.assertEqual(run.run, 'quick') # stops after correct word
        self.assertTrue(run.category[0])

    def test_build_run3(self):
        run = Run(orig, 'fox', 0) # picks up last word in orig
        run.build_run()
        self.assertEqual(run.run, 'fox')
        self.assertTrue(run.category[0])

    def test_build_run4(self):
        newPara = 'quick brown'
        run = Run(orig, para, 0) # picks up last word in para
        run.build_run()
        self.assertEqual(run.run, newPara)
        self.assertTrue(run.category[0])


    def test_build_run_punctuation1(self):
        orig = "all the punctuation is in para"
        para = "all, !the? 'punctuation,' is in! para"
        run = Run(orig, para, 0)
        run.build_run()
        self.assertEqual(run.run, para)

    def test_build_run_punctuation2(self):
        orig = "all - the 'punctuation' is!? in, orig"
        para = "all the punctuation is in orig"
        run = Run(orig, para, 0)
        run.build_run()
        self.assertEqual(run.run, para)
        self.assertTrue(run.category[0])

    def test_build_run_punctuation3(self):
        orig = "!?'punctuation at start and end'£$"
        para = "$ all the punctuation is in orig!!!"
        run = Run(orig, para, 0)
        run.build_run()
        self.assertEqual(run.run, '$ all the punctuation is in orig')
        self.assertTrue(run.category[0])



if __name__ == '__main__':
    unittest.main()
