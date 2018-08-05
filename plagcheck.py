#!/usr/bin/env python3

# Must be in same folder as the essay, reading_pack and
# filepicker.py (my own module)
#
# to check for plagiarism between 2 documents:
#              reading_pack.txt and essay.txt

"""The main engine is the find_matches() function:
    for each unique word in essay:
        for each occurance of word in essay:
            for each occurance of word in reading pack:
                check for matches in texts.    """

import get_texts
import remove_substrings
import find_matches

def main():
    level = welcome()
    textnames = get_text_names()
    rp, sa = get_texts.get_texts(textnames)
    duplicates = find_matches.find_matches(rp, sa)
    print('These are the duplicated words and phrases')
    for result in duplicates:
        print(result)

def welcome():
    print("""
        PLAGIARISM CHECKER
        
        This program finds snippets of text in an essay which have
        been copied from the reading pack.
        """)


def get_text_names():
    import filepicker  # My own module. Must be in the same directory.
    reading_pack = filepicker.filepicker('reading pack')  # User input.
    essay = filepicker.filepicker('essay')  # User input.
    texts = [reading_pack, essay]
    return texts

def results(duplicates, original_essay):
    '''Takes the original essay (for now only as .txt)
    and highlights the strings which are
    copied from the reading pack (for now as CAPS)'''
    highlighted_essay = original_essay  # For now.
    return highlighted_essay


def save_as(highlighted_essay):
    ''' Prompts for filename and saves the essay with results (for now as .txt)'''


if __name__ == '__main__':
    main()
