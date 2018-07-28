#!/usr/bin/env python3

# file picker

import os

def lsPrint():
    '''Prints a numbered list of useful files in cwd.
    Only those beginning with a letter
    and which have a '.' in them.'''
    print()    
    # get list of relevant files (not .file or directories)
    ls = os.listdir()
    dirList = []
    for item in ls:
        if item[0][0].isalpha() and '.' in item:
            dirList.append(item)
    # print out the numbered file list
    for i in range(len(dirList)):
        print(i, end='. ')
        print(dirList[i])
    print()

def pickFile(requested_file='file'):
    '''Requests a filename from user
    and returns that filename.
    If called with a "requested_file" argument,
    it will ask for that by name: eg "input file"
    '''
    print('\nPlease choose one of the following files: ')
    lsPrint()
    filename = 0
#    filename = input('Type the name of the {} here: '.format(requested_file))
#    return filename

def main():
    filename = pickFile()
    print(filename) 

if __name__ == '__main__':
    main()
