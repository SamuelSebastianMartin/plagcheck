#! /usr/bin/env/ python3


import unittest
import remove_substrings

class TestAdd(unittest.TestCase):

    def test_remove_substrings(self):
        duplicates = ['the big dog', 'the big', 'the', 'big d']
        out = ['the big dog']
        result = remove_substrings.remove_substrings(duplicates)
        self.assertEqual(result, out)

if __name__ == '__main__':
    unittest.main()
