#! /usr/bin/env/ python3

import unittest
import prune_matches


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

    def test_remove_overlaps1(self):
        # (1, 2), 2, 2) -> (1, 2)
        data = [(1, 3), (2, 3), (3, 3)]
        answer = [(1, 3)]
        result = prune_matches.remove_overlaps(data)
        self.assertEqual(result, answer)

    def test_remove_overlaps2(self):
        # When one match encroaches on another, preserve the second.
        data = [(2, 4), (3, 4), (3, 6), (4, 6), (5, 6), (6, 6)]
        answer = [(2, 4), (3, 6)]
        result = prune_matches.remove_overlaps(data)
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest(main)
