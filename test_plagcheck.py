#! /usr/bin/env/ python3

import unittest
import plagcheck

class TestPlagcheck(unittest.TestCase):


    def test_welcome(self):
        result = plagcheck.welcome()
        self.assertIn(result, [1,2,3])

if __name__ == '__main__':
    unittest.main()
