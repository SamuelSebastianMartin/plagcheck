#! /usr/bin/env/ python3


import unittest
import find_matches

class TestAdd(unittest.TestCase):

    def test_find_occurrences(self):
        text = ['zero', 'one', 'oaf', 'three', 'oaf']
        oaf = find_matches.find_occurrences('oaf', text)
        zero = find_matches.find_occurrences('zero', text)
        missing = find_matches.find_occurrences('missing', text)
        self.assertEqual(oaf, [2, 4])
        self.assertEqual(zero, [0])
        self.assertEqual(missing, [])



    def test_longest(self):
        rp = ['dud','dud', 'the', 'longest', 'match', 'dud', 'dud']
        sa = ['dud', 'the', 'longest', 'match']
        ans = ['the', 'longest', 'match']
        rp_occur = 2
        sa_occur = 1
        result = find_matches.longest(rp, sa, rp_occur, sa_occur)
        self.assertEqual(result, ans)
        # Avoid a second and longer occurance when passed the 1st occurence.
        rp = ['dud','dud', 'the', 'longest', 'match', 'dud', 'dud']
        sa = ['dud', 'the', 'longest', 'the', 'longest', 'match']
        ans = ['the', 'longest']
        result = find_matches.longest(rp, sa, rp_occur, sa_occur)
        self.assertEqual(result, ans)
        
    
    def test_find_matches(self):
        rp = ['the', 'essay', 'with', 'repeated', 'phrases', 'has', 'repeated', 'phrases']
        sa = ['some', 'repeated', 'phrases', 'in', 'essay']
        wordset = ['some', 'repeated', 'phrases', 'in', 'essay']
        ans = [['repeated', 'phrases']]
        result = find_matches.find_matches(rp, sa, wordset)
        self.assertEqual(result, ans)
        # 2 instances of same phrase in sa
        sa = ['some', 'repeated', 'phrases', 'in', 'essay', 'repeated', 'phrases']
        ans = [['repeated', 'phrases'], ['repeated', 'phrases']]
        result = find_matches.find_matches(rp, sa, wordset)
        self.assertEqual(result, ans)


if __name__ == '__main__':
    unittest(main)
