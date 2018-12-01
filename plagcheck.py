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
import prune_matches
import docx
import os


def main():
    rp_doc, rp, rp_path = get_texts.get_texts()
    sa_doc, sa, sa_path = get_texts.get_texts()

    #  Create final out document.
    out_doc = docx.Document()

    for para in sa_doc.paragraphs:
        matches = find_in_rp(rp, para)
        #print('\n\n', matches)#

        sa_indices = find_in_sa(matches, sa)
        #print(sa_indices)#
        indices = prune_matches.prune_indices(sa_indices)
        #print(indices)#

        out_doc = write_para(out_doc, sa, indices)

    out_doc.save('OUT.docx')
    os.system('libreoffice OUT.docx')


def find_in_rp(rp, para):
    text = para.text
    #print('Text = ', text)#
    para_words = get_texts.prepare_text(text)
    para_words.append('_dummy_final_word_')
    para_words.insert(0, '_dummy_first_word_')
    #print('Words= ', para_words)#

    matches = find_matches.find_matches(rp, para_words)
    return matches

def find_in_sa(matches, sa):
    spans = []
    n = 0  # Start point for search.
    for match in matches:
        srch = match.search(sa, pos=n)
        span = srch.span()
        n = span[0]  # To not research the same text. Matches are in order.
        spans.append(span)

    return spans

def write_para(out_doc, sa, indices):
    p = out_doc.add_paragraph()

    i = 0
    j = 0
    for span in indices:
        j = span[0] - 1  # End of unplagiarised section.
        p.add_run(sa[i: j])
        p.add_run(sa[span[0]: span[1]]).bold = True
        if span[1] < len(sa):
            i = span[1] + 1

    p.add_run(sa[i: -1])  # Tail end of good text.

    return out_doc


    pass

if __name__ == '__main__':
    main()
