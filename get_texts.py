#! /usr/bin/env python3

'''A module to use with 'plagcheck.py'''


import docx


def open_text(textname):
    myfile = open(textname, 'rb')  # b option allows binaries in Windows OS.
    doc = docx.Document(myfile)
    myfile.close()
    # Join docx.paragraphs into single text
    doctext = [para.text for para in doc.paragraphs]
    document = ''.join(doctext)
    print(document)
    return document


def prepare_text(text):
    '''String -> list - lowercase without punctuation.'''
    import string
    text = text.lower()
    text = "".join((char for char in text if char not in string.punctuation))
    text = text.split()
    return text


def get_texts(texts):
    """This function and sub-functions opens and prepares the two texts,
    returning clean texts, a list of unique words, and the original essay"""
#    texts = get_text_names()
    reading_pack = open_text(texts[0])
    original_essay = open_text(texts[1])
    rp = prepare_text(reading_pack)
    sa = prepare_text(original_essay)
    sa.append('#23!@23Ap9$')  # Unmatchable final value on sa
    return rp, sa


if __name__ == '__main__':
    get_texts()
