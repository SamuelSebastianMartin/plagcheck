#! /usr/bin/env python3

'''
This is to develop a regex expression to use with plagcheck.py.
It should match all punctuation, multiple spaces, capitalisation etc.
So the pattern 'cat sat' should match ['cat sat', 'Cat, sat', 'cat was sat']
'''
import re

def main():
    sa, matches = set_up()
    link = define_link()
    runs = find_run(sa, matches, link)
    for run in runs:
        print(run)  # For now.


def set_up():
    '''creates sa and rp object for testing purposes only'''
    sa = 'The cat, Tom, sat on the mat.'
    matches = ['sat on the', 'the cat']
    return (sa, matches)


def define_link():
    '''Defines the regex to be used for joining search terms'''
    link = r'\s'
    return link

def find_run(sa, matches, link):
    '''This is were the testing really happens'''
    runs = []
    for match in matches:
        match_words = match.split()
        search_str = link.join(match_words)

        regex = re.compile(search_str, re.IGNORECASE)
        regout = regex.search(sa)
        run = regout.group()

        runs.append(run)
    return runs

if __name__ == '__main__':
    main()
