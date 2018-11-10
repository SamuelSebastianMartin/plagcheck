#! /usr/bin/env python3

from operator import itemgetter  # To sort tuples by 2nd number.

def prune_indices(matches):
    ordered_matches = sort_second(matches)
    indices = remove_overlaps(ordered_matches)

    return indices


def sort_second(matches):
    '''Sorts list of tuples by second value:
    [(1, 2), (2, 1)] -> [(2, 1), (1, 2)].'''
    matches.sort(key=itemgetter(1))

    return matches


def remove_overlaps(ordered_matches):
    '''[(1, 3), (2, 3), (3, 3)] -> [(1, 3)]
    Note, in the case of an overlap, tuples are removed
    from the first range, and the later is left intact:
    [(2, 4), (3, 4), (3, 6), (4, 6), (5, 6), (6, 6)] ->
    [(2, 4),         (3, 6), (4, 6), (5, 6), (6, 6)]'''
    i = 1
    while i <= len(ordered_matches)-1:
        if ordered_matches[i-1][1] == ordered_matches[i][1]:
            ordered_matches.remove(ordered_matches[i])
        else:
            i += 1


    return ordered_matches
