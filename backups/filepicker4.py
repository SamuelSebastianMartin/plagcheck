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
    return dirList

def inputSentinelInt(From=0, To=999, message='Please pick a number: '):
    ''''Provides a sentinel restriction on input
    to avoid non-integers or out-of-range values.
    Defaults are between From 0 To 999
    but these can be changed with 
    "From=-1, To=8" for example
    There is an optional "message=" argument, too -
    the default is "Please pick a number".
    It returns the number as int'''
    number = 'a' # dummy value
    # control imput to numer withing correct range
    while number.isnumeric() == False or int(From) > int(number) or int(number) > int(To):
        number = input(message)
    number = int(number)
    return number


def pickFile(requested_file='file'):
    '''Requests a filename from user
    and returns that filename.
    If called with a "requested_file" argument,
    it will ask for that by name: eg "input file"
    '''
    print('\nPlease choose one of the following files: ')
    dirList = lsPrint() # list relevant files
    #set values for input sentinel funtion
    lower = 0
    upper = len(dirList)-1
    message = 'Please chose the NUMBER of your {} '.format(requested_file)
    filenumber = inputSentinelInt(lower, upper, message)
    filenumber = int(filenumber)
    filename = dirList[filenumber]
    print('You chose file {}, which is {}'.format(filenumber, filename))

    return filename

def main():
    filename = pickFile()
    print(filename) 

if __name__ == '__main__':
    main()
