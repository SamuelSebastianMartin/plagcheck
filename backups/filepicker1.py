#!/usr/bin/env python3

# file picker

import os

def lsPrint():
    '''Prints a list of files in cwd.
    Only those beginning with a letter
    and which have a '.' in them.'''
    print()    
    ls = os.listdir()
    for i in range(len(ls)):
        item = ls[i]
        if item[0][0].isalpha():
            if '.' in item:
                print(ls[i])

def pickFile(requested_file='file'):
    '''Requests a filename from user
    and returns that filename.
    If called with a "requested_file" argument,
    it will ask for that by name: eg "input file"
    '''
    print('Please choose one of the following files: ')
    lsPrint()
    filename = input('Type the name of the {} here: '.format(requested_file))
    return filename

def main():
    filename = pickFile()
    print(filename) 

if __name__ == '__main__':
    main()
