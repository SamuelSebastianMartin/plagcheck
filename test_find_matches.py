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



    def test_longest_match1(self):
        # find match at end of sa
        rp = ['dud','dud', 'the', 'longest', 'match', 'dud', 'dud']
        sa = ['dud', 'the', 'longest', 'the', 'longest', 'match']
        ans = ['the', 'longest', 'match']
        rp_occur = 2
        sa_occur = 3
        result = find_matches.longest_match(rp, sa, rp_occur, sa_occur)
        self.assertEqual(result, ans)


    def test_longest_match2(self):
        # Avoid a second and longer occurance when passed the 1st occurence.
        rp = ['dud','dud', 'the', 'longest', 'match', 'dud', 'dud']
        sa = ['dud', 'the', 'longest', 'the', 'longest', 'match']
        ans = ['the', 'longest']
        rp_occur = 2
        sa_occur = 1
        result = find_matches.longest_match(rp, sa, rp_occur, sa_occur)
        self.assertEqual(result, ans)

    def test_longstring_only1(self):
       matches = [['the', 'bus'], ['the']]
       ans = ['the', 'bus']
       result = find_matches.longstring_only(matches)
       self.assertEqual(result, ans)

    def test_longstring_only2(self):
       matches = [['bus'], ['bus']]
       ans = ['bus']
       result = find_matches.longstring_only(matches)
       self.assertEqual(result, ans)

    def test_find_matches1(self):
        rp = ['the', 'essay', 'with', 'repeated', 'phrases', 'has', 'repeated', 'phrases']
        sa = ['some', 'repeated', 'phrases', 'in', 'sa']
        wordset = ['some', 'repeated', 'phrases', 'in', 'essay']
        ans = [['repeated', 'phrases']]
        result = find_matches.find_matches(rp, sa)
        self.assertEqual(result, ans)

    def test_find_matches2(self):
        # 2 instances of same phrase in sa
        rp = ['the', 'essay', 'with', 'repeated', 'phrases', 'has', 'repeated', 'phrases']
        sa = ['some', 'repeated', 'phrases', 'in', 'sa', 'repeated', 'phrases', 'A£:@784!']  # Last item must be junk
        ans = [['repeated', 'phrases'], ['repeated', 'phrases']]
        result = find_matches.find_matches(rp, sa)
        self.assertEqual(result, ans)


if __name__ == '__main__':
    unittest(main)
