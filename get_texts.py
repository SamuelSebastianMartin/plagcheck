#! /usr/bin/env python3

'''A module to use with 'plagcheck.py'''


import docx
import logging

logging.basicConfig(level=logging.CRITICAL)

def open_text(textname):
    doc = docx.Document(textname)  # Create a Document object.
    logging.debug("Num of paras - {}".format(len(doc.paragraphs)))
    # Join docx.paragraphs into single text
    doctext = [para.text for para in doc.paragraphs]
    document = ''.join(doctext)
    logging.debug("whole text - {}".format(document))
    return document


def prepare_text(text):
    '''String -> list - lowercase without punctuation.'''
    import string
#    text = text.lower()
#    text = "".join((char for char in text if char not in string.punctuation))
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
    return rp, sa, original_essay


if __name__ == '__main__':
    get_texts()
