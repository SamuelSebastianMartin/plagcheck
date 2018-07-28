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


if __name__ == '__main__':
    unittest.main()
