#! /usr/bin/env/ python3

import unittest
import plagcheck

class TestPlagcheck(unittest.TestCase):


    def test_welcome(self):
        result = plagcheck.welcome()
        self.assertIn(result, [1,2,3])

    def test1_find_matches(self):
        '''finds all and only the matched text'''
        rp = 'wobbly elephant legs'
        sa = 'wobbly elephant'
        unique_words = ['wobbly', 'elephant', 'legs']
        answer = ['wobbly elephant', 'elephant']
        result = plagcheck.find_matches(rp, sa, unique_words)
        self.assertEqual(result, answer)

    def test2_find_matches(self):
        '''includes leading small words, like 'the' or 'a'.'''
        rp = 'the wobbly elephant legs'
        sa = 'the wobbly elephant'
        unique_words = ['wobbly', 'elephant', 'legs']
        answer = ['the wobbly elephant', 'the elephant']
        result = plagcheck.find_matches(rp, sa, unique_words)
        self.assertEqual(result, answer)

    def test3_find_matches(self):
        '''checks functioning with last word in text'''
        rp = 'wobbly elephant legs'
        sa = 'legs'
        unique_words = ['legs']
        answer = ['legs']
        result = plagcheck.find_matches(rp, sa, unique_words)
        self.assertEqual(result, answer)

    def test4_find_matches(self):
        '''checks that a second matching phrase is not missed
        if it is a subset of a larger one. eg if the phrases
        "fat bottomed girls" and "fat bottomed" are both in
        the essay, will they both appear in the results'''
        rp = 'fat bottomed girls you make this rocking'
        sa = 'fat bottomed blah blah fat bottomed girls'
        unique_words = ['fat', 'bottomed', 'blah', 'girls']
        result = plagcheck.find_matches(rp, sa, unique_words)
        self.assertIn("['fat bottomed']", result)
        self.assertIn("['fat bottomed girls']", result)
if __name__ == '__main__':
    unittest.main()
