#! /usr/bin/env python3

'''A module to use with 'plagcheck.py'''

#def get_text_names():
#    import filepicker  # My own module. Must be in the same directory.
#    reading_pack = filepicker.filepicker('reading pack')  # User input.
#    essay = filepicker.filepicker('essay')  # User input.
#    texts = [reading_pack, essay]
#    return texts


def open_text(text):
    myfile = open(text, 'r')
    document = myfile.read()
    myfile.close()
    return document


def word_set(sa):
    unique_essay_words = list(set(sa))
    return unique_essay_words


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
    wordset = word_set(sa)
    return rp, sa, original_essay, wordset


if __name__ == '__main__':
    get_texts()
