#! /usr/bin/env python3

from operator import itemgetter  # To sort tuples by 2nd number.


def prune_indices(matches):
    '''Input is a list of tuples, each containing the start and end point
    of a match in the essay (sa). This module sorts these tuples by the
    second value (i.e. the end point of each matched sectioin) and then
    removes duplicates. So ['the cat', 'cat'] would become ['the cat'],
    but in numbers, of course: [(1, 2), (2, 2)] becomes [(1, 2)].
    '''
    ordered_matches = sort_second(matches)
    indices = remove_subsets(ordered_matches)
    indices = split_overlaps(indices)
    indices = remove_nesting(indices)

    return indices


def sort_second(matches):
    '''Sorts list of tuples by second value:
    [(2, 3), (1, 3)] -> [(1, 3), (2, 3)] and
    [(1, 2), (2, 1)] -> [(2, 1), (1, 2)].'''
    matches = list(set(matches))        # Remove duplicates
    matches.sort()                      # sort by tuple[0]
    matches.sort(key=itemgetter(1))     # sort by tuple[1]

    print('sorted matches :', matches)#
    return matches


def remove_subsets(ordered_matches):
    # Make overlaps yield to the longest???
    '''[(1, 3), (2, 3), (3, 3)] -> [(1, 3)]
    Note, in the case of an overlap, tuples are removed
    from the first range, and the later is left intact:
    [(2, 4), (3, 4), (3, 6), (4, 6), (5, 6), (6, 6)] ->
    [(2, 4)   ....   (3, 6)   ....    ....    .... ]'''
    i = 1
    while i <= len(ordered_matches)-1:
        if ordered_matches[i-1][1] == ordered_matches[i][1]:
            ordered_matches.remove(ordered_matches[i])
        else:
            i += 1

    print('ordered_matches :', ordered_matches)#
    return ordered_matches

def split_overlaps(spans):
    '''When 2 runs overlap, the longest is preserved.
    eg [(1, 5), (4, 6)] -> [(1, 5), (6, 6)]
    Note: cannot be used if span[0] are the same: [(1, 5), (1, 6)]'''
    for i in range(0, len(spans)-1):
        if spans[i][1] >= spans[i+1][0] and spans[i][0] < spans[i+1][0]:
            spans[i], spans[i+1] = yield_longest(spans[i], spans[i+1])
    return spans


def yield_longest(first, second):
    '''Takes two overlapping spans and returns a non-overlapping equivalent.
    The longest is preserved. Equality favours the second.'''
    if (first[1] - first[0]) > (second[1] - second[0]):
        second = (first[1] +1, second[1])
    else:
        first = (first[0], second[0] -1)
    return first, second


def remove_nesting(items):
    # FAIL
    ''' [(1, 3), (0, 4)] -> [(0, 4)] and
        [(0, 3), (0, 4)] -> [(0, 4)]
    After sort_second(), a span may be fully comprehended in the
    span to its right. This will remove such nested spans'''
    unnested = items.copy()
    for i in range(len(items)):
        print(items[i-1][0], items[i][0])
        if items[i-1][1] < items[i][1] and items[i-1][0] >= items[i][0]:
            print('removing ', items[i-1])
            unnested.remove(items[i-1])
    print('unnested :', unnested)#
    return unnested
