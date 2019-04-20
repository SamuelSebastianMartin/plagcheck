#! /usr/bin/env python3

from unittest import TestCase
import unittest

import build_document


class TestTextSpan(TestCase):

    def test_TextSpan(self):
        sp = build_document.TextSpan((23, 136), True)
        self.assertEqual(sp.i, 23)
        self.assertEqual(sp.j, 136)
        self.assertEqual(sp.plag, True)


class TestSpansToTextspans(TestCase):

    def setUp(self):
        self.sa_spans = [(15, 30), (49, 55), (70, 100)]

    def test_spans_to_textspans_len(self):
        sps = build_document.spans_to_textspans(self.sa_spans)
        self.assertEqual(len(sps), len(self.sa_spans))

    def test_spans_to_textspans_plag(self):
        sps = build_document.spans_to_textspans(self.sa_spans)
        for sp in sps:
            self.assertTrue(sp.plag)

    def test_spans_to_textspans_indices(self):
        sps = build_document.spans_to_textspans(self.sa_spans)
        for n in range(len(sps)):
            self.assertEqual(sps[n].i, self.sa_spans[n][0])
            self.assertEqual(sps[n].j, self.sa_spans[n][1])


class TestBuildDocuments(TestCase):

    def setUp(self):
        self.sa_spans = [(6, 21), (23, 27), (36, 40), (45, 49)]
        self.text = "Since there's no hope, come, let us kiss and part."

    def test_first_item(self):
        # The first index must be zero
        outspans = build_document.build_document('', [(23, 119)])
        self.assertEqual(outspans[0].i, 0)

    def test_last_item(self):
        # The last index must be len(text) -1
        outspans = build_document.build_document('dummy.', [(0, 5)])
        self.assertEqual(outspans[-1].j, len('dummy.')-1)

    def test_full_text_len(self):
        # The combined TextSpan text is the same length as 'text'.
        print(self.text)  ##
        outspans = build_document.build_document(self.text, self.sa_spans)
        newtext = ''
        for sp in outspans:
            newtext = newtext + newtext[sp.i: sp.j]
        self.assertEqual(newtext, 0)


if __name__ == '__main__':
    unittest.main()
