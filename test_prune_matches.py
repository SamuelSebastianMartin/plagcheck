#! /usr/bin/env/ python3

import unittest
import prune_matches
import os


class TestAdd(unittest.TestCase):

    def test_prune_indices(self):
        data = [(34, 35), (35, 35), (2, 3), (3, 3)]
        answer = [(2, 3), (34, 35)]
        result = prune_matches.prune_indices(data)
        self.assertEqual(result, answer)

    def test_sort_second(self):
        # Sorts list of tuples by second value.
        data = [(1, 2), (2, 1)]
        answer = [(2, 1), (1, 2)]
        result = prune_matches.sort_second(data)
        self.assertEqual(result, answer)

    def test_remove_subsets1(self):
        # (1, 2), 2, 2) -> (1, 2)
        data = [(1, 3), (2, 3), (3, 3)]
        answer = [(1, 3)]
        result = prune_matches.remove_subsets(data)
        self.assertEqual(result, answer)

    def test_remove_subsets2(self):
        # When one match encroaches on another, preserve the second.
        data = [(2, 4), (3, 4), (3, 6), (4, 6), (5, 6), (6, 6)]
        answer = [(2, 4), (3, 6)]
        result = prune_matches.remove_subsets(data)
        self.assertEqual(result, answer)

    def test_split_overlaps(self):
        data = [(1, 7), (6, 9)]
        answer = [(1, 7), (8, 9)]
        result = prune_matches.split_overlaps(data)
        self.assertEqual(result, answer)

    def test_yield_longest1(self):
        big = (1, 7)
        small = (6, 9)
        first, second = prune_matches.yield_longest(big, small)
        self.assertEqual(first, (1, 7))
        self.assertEqual(second, (8, 9))

    def test_yield_longest2(self):
        big = (1, 7)
        small = (6, 8)
        first, second = prune_matches.yield_longest(big, small)
        self.assertEqual(second, (8, 8))

    def test_remove_nesting1(self):
        # Half nested overlap
        data = [(2, 3), (2, 8)]
        answer = [(2, 8)]
        result = prune_matches.remove_nesting(data)
        self.assertEqual(result, answer)

    def test_remove_nesting2(self):
        # When frist span is contained within second span - removes the first.
        data = [(1, 2), (0, 3)]
        answer = [(0, 3)]
        result = prune_matches.remove_nesting(data)
        self.assertEqual(result, answer)

    def test_remove_nesting3(self):
        # Multiple concentric nesting.
        data = [(2, 3), (1, 4), (0, 5)]
        answer = [(0, 5)]
        result = prune_matches.remove_nesting(data)
        self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest(main)
