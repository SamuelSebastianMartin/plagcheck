#! /usr/bin/env python3

'''A module to use with 'plagcheck.py'''

def open_text(text):
    myfile = open(text, 'r')
    document = myfile.read()
    myfile.close()
    return document
