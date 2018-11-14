#! /usr/bin/env python3

'''A module to use with 'plagcheck.py'''


import docx



def filepicker():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path

def open_text(file_path):
    doc_object = docx.Document(file_path)  # Create a Document object.
    return doc_object


def prepare_text(text):
    '''String -> list - lowercase without punctuation.'''
    import string
    text = text.lower()
    text = "".join((char for char in text if char not in string.punctuation))
    para_words = text.split()
    return para_words


def get_texts():
    '''Function name is a deletable legacy of previous versions'''
    pass


if __name__ == '__main__':
    get_texts()
