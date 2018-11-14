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


def doctotext(doc_object):
    text_list = []
    for para in doc_object.paragraphs:
        text_list.append(para.text)
    text = '\n'.join(text_list)
    return text


def prepare_text(text):
    '''String -> list - lowercase without punctuation.
    Not called in get_texts(), but called from plagcheck.main()'''
    import string
    text = text.lower()
    text = "".join((char for char in text if char not in string.punctuation))
    para_words = text.split()
    return para_words


def get_texts():
    '''Selects and returns docx objects and text object.'''
    file_path = filepicker()
    doc_object = open_text(file_path)
    text = doctotext(doc_object)
    return doc_object, text


if __name__ == '__main__':
    get_texts()
