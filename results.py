#! /usr/bin/env/ python3

import docx


def results(shortlist):
    for result in shortlist:
        print(' '.join(result))
