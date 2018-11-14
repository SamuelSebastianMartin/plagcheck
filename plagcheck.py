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
    rp_doc, rp = get_texts.get_texts()
    sa_doc, sa = get_texts.get_texts()
    para_words = get_texts.prepare_text(sa)

    for para in sa_doc.paragraphs:
        text = para.text
        para_words = get_texts.prepare_text(text)
        print(para_words)
        print()


if __name__ == '__main__':
    main()
