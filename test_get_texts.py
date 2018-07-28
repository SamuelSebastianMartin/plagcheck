#! /usr/bin/env/ python3


import unittest
import get_texts

class TestAdd(unittest.TestCase):

    def test_open_text(self):
        text = get_texts.open_text('get_texts.py')
        t_type = type(text)
        s_type = type('random string')
        self.assertEqual(t_type, s_type)

if __name__ == '__main__':
    unittest.main()
