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
import find_matches

def main():
    level = welcome()
    textnames = get_text_names()
    rp, sa = get_texts.get_texts(textnames)
    duplicates = find_matches.find_matches(rp, sa)
    print('These are the duplicated words and phrases')
    for result in duplicates:
        critical_length = 2
        if len(result) > critical_length:
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



if __name__ == '__main__':
    main()
