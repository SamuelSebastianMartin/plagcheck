#! /usr/bin/env/ python3

a = 'abcdefghijklm'
b = 'abcdefgj'

class Match:
    def __init__(self, a, b, j):
        self.j = j


def finder(match, a, b):
        if b[:match.j] not in a:
            print('not in', match.j, b[:match.j])
            return match.j
        else:
            print('ok', match.j, b[:match.j])
            match.j += 1
            if match.j < len(b)+1:
                finder(match, a, b)
            else:
                return match.j

match = Match(a, b, 1)
finder(match, a, b)
print(match.j)

match = Match(a, b, 0)
finder(match, a, a)
print(match.j)
