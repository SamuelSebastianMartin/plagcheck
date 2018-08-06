#! /usr/bin/env/ python3


import unittest
import get_texts

class TestAdd(unittest.TestCase):

    def test_open_text(self):
        # Using this file as only securechoice is directory list.
        text = get_texts.open_text('get_texts.py')
        # Text is a string.
        t_type = type(text)
        s_type = type('random string')
        self.assertEqual(t_type, s_type)
        # Not  empty. 
        L = len(text)
        self.assertNotEqual(L, 0)

    def test_prepare_text(self):
        text = 'The. fiSH & chips!\n me@mail!!! (3): www.dog'
        out = ['the', 'fish', 'chips', 'memail', '3', 'wwwdog']
        result = get_texts.prepare_text(text)
        self.assertEqual(result, out)

if __name__ == '__main__':
    unittest.main()
